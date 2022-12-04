<template>
  <carousel-3d
    id="ranking"
    :start-index="1"
    :controls-visible="true"
    :width="500"
    :height="800"
    :display="3"
    :space="700"
    :autoplay="true"
    :autoplay-timeout="2000"
    :autoplay-hover-pause="true"
    :controls-prev-html="'&#10092;'"
    :controls-next-html="'&#10093;'"
    :controls-width="30"
    :controls-height="100"
  >
    <slide :index="0" :key="0" :id="0">
      <div id="first-intro">
        <img
          class="first-img"
          src="https://www.mosaicmarble.com/uploads/2013/07/movie-face-on-a-poster.jpg"
        />
        <caption class="first-caption">
          10 TRENDING MOVIES
        </caption>
      </div>
    </slide>
    <slide
      v-for="(trendingMovie, index) in trendingMovies"
      :index="index + 1"
      :key="trendingMovie.length"
      :id="index + 1"
    >
      <div @click="pushMovieDetail(trendingMovie.id)">
        <span>{{ index + 1 }}</span>

        <img
          :src="
            'https://image.tmdb.org/t/p/original' + trendingMovie.poster_path
          "
        />
        <caption>
          {{
            trendingMovie.title
          }}
        </caption>
      </div>
    </slide>
  </carousel-3d>
</template>

<script>
import { Carousel3d, Slide } from "vue-carousel-3d"
import axios from "axios"
export default {
  name: "RankingCarousel",
  components: {
    Carousel3d,
    Slide,
  },
  data() {
    return {
      trendingMovies: [],
    }
  },
  // props: {
  //   trendingMovies: Array,
  // },
  methods: {
    getTrendingMovies() {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/movies/ranking/0/",
      })
        .then((response) => {
          this.trendingMovies = response.data
        })
        // axios({
        //   method: "get",
        //   url: "https://api.themoviedb.org/3/movie/top_rated",
        //   params: {
        //     api_key: "f7fb3966fa04584f38174fe8f31397a5",
        //   },
        // })
        .then((response) => {
          // this.trendingMovies = response.data;
          this.trendingMovies = response.data.results
        })
        .catch((error) => {
          console.log(error)
        })
    },
    pushMovieDetail(mov_id) {
      this.$store.dispatch("pushMovieDetail", mov_id)
    },
  },
  created() {
    this.getTrendingMovies()
    console.log("created")
  },
  updated() {
    let evt = document.createEvent("HTMLEvents")
    evt.initEvent("resize", true, false)
    window.dispatchEvent(evt)
  },
}
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Anton&display=swap");
#ranking {
  width: 100%;
  height: 30%;
  padding-top: 50px;
  padding-bottom: 50px;
}
.carousel-3d-container {
  padding-block: 10%;
}
#ranking .carousel-3d-slide {
  background-color: transparent;
  text-align: center;
  overflow: visible;
}
#ranking .carousel-3d-slide.current > img {
  overflow: visible;
  max-height: 80%;
}
#ranking .carousel-3d-slide.current img:not(.first-img):hover {
  filter: brightness(20%);
}
#ranking .carousel-3d-slide.current img:hover + caption {
  display: block;
}
#ranking .carousel-3d-slide span {
  font-family: "anton";
  font-size: 7rem;
  font-weight: bolder;
  max-width: 100%;
  font-style: italic;
  position: absolute;
  top: -10%;
  left: 2%;
  z-index: 1000;
}
#ranking .carousel-3d-slide div {
  margin: 0;
}
#ranking .first-img {
  /* border-radius: 30%; */
  border: none;
  filter: brightness(20%);
  box-shadow: 0px 0px 20px 5px;
  height: 700px;
}
#ranking .first-caption {
  font-family: "anton";
  display: block;
  position: absolute;
  background-color: transparent;
  color: #fff;
  position: absolute;
  top: 35%;
  font-size: 3rem;
  min-width: 100%;
  box-sizing: border-box;
  text-align: center;
}

#ranking caption {
  display: none;
  position: absolute;
  background-color: transparent;
  color: #fff;
  position: absolute;
  bottom: 50%;
  padding: 15px;
  font-size: 3rem;
  min-width: 100%;
  box-sizing: border-box;
  text-align: center;
}
</style>
