<template>
  <v-dialog v-model="show" width="50%" max-width="400px">
    <v-card class="container">

      <v-card-title class="font-set align-center justify-content-between">
        <div class="container d-flex align-center justify-content-between">
        <span class="text-h4">{{reviewDetail.title}} <br></span>
      <div v-if="likeReview">
        <v-btn class="ma-3" fab dark color="deep-purple accent-2" @click="likeUnlikeReview" elevation="1">
          <v-icon dark>mdi-thumb-up</v-icon>
        </v-btn>
      </div>
      <div v-else>
        <v-btn class="ma-3" text fab color="secondary" @click="likeUnlikeReview" elevation="1">
          <v-icon >mdi-thumb-up</v-icon>
        </v-btn>
      </div>
      </div>
      </v-card-title>
      <div class="d-flex justify-content-between align-center">
      <v-card-subtitle class="text-h6 float-left">
        {{reviewDetail.movie.title}}
      </v-card-subtitle>
      <div class="">
        <v-rating :value="reviewDetail.rank" color="amber" dense half-increments readonly size="20"></v-rating>
      </div>
      <!-- 작성글 좋아요 버튼 -->
      </div>
      <v-divider></v-divider>
      <div class="container d-flex justify-content-between">

        <div class="grey--text">
          <v-avatar>
            <img
              :src="`http://127.0.0.1:8000${reviewDetail.user.profile_path}`"
              alt="profile_img"
            >
          </v-avatar>
          &nbsp;&nbsp;
          <a href="#" @click="openAnotherUserProfile(reviewDetail.user.id, $event)">{{reviewDetail.user.nickname}}</a>
        </div>
        <div class="d-flex grey--text pt-2">작성일 : {{reviewDetail.updated_at.slice(0,10)}}</div>
      </div>
      
      <!-- 오른쪽으로 보내줘요............................ -->
      <v-divider></v-divider>
      <v-card-text class="text-body-1" style="color: black">
        {{reviewDetail.content}}
      </v-card-text>
      <v-divider></v-divider>
      <!-- comment 다는 곳 -->
      <v-form ref="form" class="container align-self-end" @submit.prevent="createComment">
        <div class="d-flex">
        <v-text-field label="comment" v-model="comment"></v-text-field>
          <v-btn
            class="mt-3"
            fab
            dark
            color="indigo"
            small
            >
          <v-icon class="" dark @click="createComment">
            mdi-plus
          </v-icon>
        </v-btn>
        </div>
      </v-form>
      
      <v-simple-table>
      <!-- <v-simple-table v-scroll.self="onScroll" height="268px"> -->
        <template v-slot:default>
          <thead>
            <tr>
              <th class="text-left">
                NickName
              </th>
              <th class="text-left">
                comment
              </th>
              <th class="text-left">
                delete
              </th>
            </tr>
          </thead>
          <tbody>
            <!-- 이거뭐야,,,,? -->
            <!-- comment 자리 -->
            <tr v-for="comment in comments" :key="comment.id">
              <td>{{ comment.user.nickname }}</td>
              <td>{{ comment.comment }}</td>
              <!-- 삭제버튼 -->
              <td>
                <div v-if="comment.user.nickname==userInfo.nickname" @click="deleteComment(comment)">
                  <v-btn
                    elevation="2"
                    x-small
                    icon
                    color="pink"
                  >
                    <v-icon>mdi-minus</v-icon>
                  </v-btn>
                </div>
              </td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
      <div class="text-center">
        <!-- 댓글 페이지네이션 구현하기 -->
        <!-- <v-pagination
          v-model="page"
          :length="4"
          circle
        ></v-pagination> -->
      </div>
      <v-card-actions>
        <div class="d-flex">
          <v-btn text @click="show=false">Close</v-btn>
          <div v-if="reviewDetail.user.id==userInfo.id">
            <v-btn text @click="reviewEditOpen=true">Edit</v-btn>
            <v-btn text @click="deleteReview">Delete</v-btn>
          </div>
        </div>
      </v-card-actions>

    </v-card>
    <MovieReviewEdit
      v-model="reviewEditOpen"
    ></MovieReviewEdit>
  </v-dialog>
</template>

<script>
import {mapState} from 'vuex'
import MovieReviewEdit from './MovieReviewEdit.vue'
  export default {
  name: 'MovieDetailReview',
  data : function(){
    return{
      comment:null,
      reviewEditOpen:false,
    }
  },
  components: { 
    MovieReviewEdit 
  },
  props: {
    value: Boolean,
  },
  methods: {
    likeUnlikeReview : function(){
      const reviewPk = this.reviewDetail.id
      this.$store.dispatch('review/likeUnlikeReview', reviewPk)
      this.$store.dispatch('getMovieDetail/movieDetail')
      // console.log(this.reviewDetail)
    },
    openAnotherUserProfile : function(otherUserPk, event){
      event.preventDefault()
      this.$store.dispatch('login/getOtherUserInfo',otherUserPk)
      this.$router.push({name : 'Profile'})
    },
    deleteReview:function(){
      let reviewPk = this.reviewDetail.id
      this.$store.dispatch('review/deleteReview',reviewPk)
      // location.reload()
    },
    createComment : function(event){
      event.preventDefault()
      let commentData = {
        'reviewPk' :this.reviewDetail.id,
        'comment' : this.comment
      }
      this.$store.dispatch('comment/createComment',commentData)
      this.comment = null
    },
    deleteComment : function(comment){
      this.$store.dispatch('comment/deleteComment', comment)
    }
  },
  computed: {
    ...mapState('review', ['reviewDetail','likeReview']),
    ...mapState('comment', ['comments']),
    ...mapState('login', ['userInfo']),
    show: {
      get() {
        return this.value
      },
      set(value) {
        this.$emit('input', value)
      }
    }
  }
  }
</script>

<style scoped>
  .font-set {
    font-family: 'IBM Plex Sans KR', sans-serif !important;
  }
</style>