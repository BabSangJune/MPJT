<template>
<div>
  <div class="welcome">
    <p>Box Office</p>
  </div>

  <div class="img-box">
    <div class="real-box">
      <span :style="`--i:${index+1}`" v-for="(trendmovie,index) in trendMovies" :key="index">
        <figure class="hover-effect" @click="movieDetail(trendmovie.id)">
          <img :src="`https://image.tmdb.org/t/p/original${trendmovie.poster_path}`">
            <figcaption class="">
              <h3>{{index+1}}</h3>
              <h5>{{trendmovie.title}}</h5>
              <!-- <h5>{{trendmovie.overview}}</h5> -->
            </figcaption>
          
        </figure>
      </span>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'MovieBoxOffice',
  data : function(){
    return{
      trendMovies : null,
    }
  },
  methods :{
    movieDetail: function (movieid) {
        let movieId = movieid
        this.$store.dispatch('getMovieDetail/setMovieId', movieId)
        this.$store.dispatch('recommendMovies/getRecommend', movieId)
        this.$router.push({
          name: 'MovieDetail'
        })
    }
  },
  created :function(){
    // 환경변수로 숨기기
    const API_KEY='33e4ef19e015d915281ddd6881f93178'
    axios({
      method : 'get',
      url : `https://api.themoviedb.org/3/trending/movie/week?api_key=${API_KEY}`
    })
      .then((res)=>{
        // console.log(res.data.results)
        this.trendMovies = res.data.results.slice(0,8)
        this.$store.dispatch('saveMovies/saveMovies',res.data.results)
      })

  }
}
</script>

<style scoped>
@import url(https://fonts.googleapis.com/css?family=Source+Sans+Pro);
.welcome {
    z-index: 999;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .welcome p {
    position: relative;
    /* font-family: sans-serif; */
    /* color: white; */
    text-transform: uppercase;
    font-size: 2em;
    letter-spacing: 4px;
    overflow: hidden;
    background: linear-gradient(90deg, #000, #fff, #000);
    background-repeat: no-repeat;
    background-size: 70%;
    animation: animate 2s linear infinite;
    -webkit-text-fill-color: rgba(255, 255, 255, 0);
    -webkit-background-clip: text;
  }

  @keyframes animate
  {
    0%
    {
      background-position: -400%;
    }
    100%
    {
      background-position: 300%;
    }
  }

.hover-effect {
  /* font-family: 'Source Sans Pro', sans-serif; */
  position: relative;
  overflow: hidden;
  margin: 10px;
  min-width: 160px;
  max-width: 100px;
  width: 100%;
  color: #ffffff;
  text-align: left;
  font-size: 16px;
  background: linear-gradient(
  rgba(143, 143, 143, 0.7), 
  rgba(0, 0, 0, 0.9));
  /* background-color: rgba(41, 41, 41, 0.803); */
}

.hover-effect * {
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  -webkit-transition: all 0.45s ease;
  transition: all 0.45s ease;
}

.hover-effect img {
  vertical-align: top;
  max-width: 100%;
  backface-visibility: hidden;
}

.hover-effect figcaption {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1;
  align-items: center;
  bottom: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.hover-effect h3,
.hover-effect h5 {
  margin: 0;
  opacity: 0;
  letter-spacing: 1px;
}

.hover-effect h3 {
  -webkit-transform: translateY(-100%);
  transform: translateY(-100%);
  text-transform: uppercase;
  font-weight: 400;
}

.hover-effect h5 {
  font-weight: normal;
  font-style: italic;
  color: rgb(255, 255, 255);
  -webkit-transform: translateY(100%);
  transform: translateY(100%);
}

.hover-effect a {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 1;
}

.hover-effect:hover > img,
.hover-effect.hover > img {
  opacity: 0.1;
}

.hover-effect:hover h3,
.hover-effect.hover h3,
.hover-effect:hover h5,
.hover-effect.hover h5 {
  -webkit-transform: translateY(0);
  transform: translateY(0);
  opacity: 1;
}

  img {
    /* width: 200px;
    height: 200px; */
  }
  .img-box {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 40vh;
    /* background: #000f; */
  }
  .real-box {
    position: relative;
    width: 230px;
    height: 230px;
    transform-style: preserve-3d;
    animation: animate2 30s linear infinite;
  }

  @keyframes animate2
  {
    0%
    {
      transform: perspective(1000px) rotateY(0deg);
    }
    100%
    {
      transform: perspective(1000px) rotateY(360deg);
    }
  }


  .real-box span {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    transform-origin: center;
    transform-style: preserve-3d;
    transform: rotateY(calc(var(--i) * 45deg )) translateZ(400px);
    -webkit-box-reflect: below 0px linear-gradient(transparent, transparent, #0008);
  }

  .real-box span img {
    position: relative;
    top: 0;
    left: 0;
    widows: 100%;
    height: 100%;
    object-fit: cover;
    
  }

</style>