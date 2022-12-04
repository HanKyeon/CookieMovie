<template>
  <div>
    <swiper class="swiper m-2" :options="swiperOption">
      <swiper-slide
        v-for="(movie, idx) in recommendMovies"
        :key="`rec-mov-${idx}`"
        :id="`recmov-${idx}`"
        class="p-1"
        :class="idx === 0 ? ['mx-3'] : ['mr-3']"
      >
        <img
          :src="`https://image.tmdb.org/t/p/original${movie?.poster_path}`"
          style="height: 100%; width: 100%"
          @click="pushMovieDetail(movie.id)"
          class="collection-img-hov p-1"
        />
      </swiper-slide>
      <!-- <div class="swiper-pagination" slot="pagination"></div> -->
    </swiper>
    <hr />
    <hr />
    <hr />
  </div>
</template>

<script>
import { Swiper, SwiperSlide } from "vue-awesome-swiper"
import "swiper/css/swiper.css"
import axios from "axios"

export default {
  name: "MovieRecommendations",
  components: {
    Swiper,
    SwiperSlide,
  },
  data() {
    return {
      swiperOption: {
        slidesPerView: 6,
        spaceBetween: 30,
        centeredSlides: false,
        pagination: {
          el: ".swiper-pagination",
          clickable: true,
        },
      },
      recommendMovies: null,
      recommendMovies2: null,
      recommendMovies3: null,
      recommendMovies4: null,
    }
  },
  methods: {
    getRecommend() {
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/movies/recommend/`,
        headers: {
          Authorization: this.$store.state.token, // => 선택. 있으면 유저가 점수를 높게 준 영화를 함께 높게 준 유저들이 높게 준 영화들 중에 내가 안 본 영화 추천. 없으면 랜덤
        },
        data: {},
      }).then((res) => {
        this.recommendMovies = res.data
      })
    },
    pushMovieDetail(mov_id) {
      this.$store.dispatch("pushMovieDetail", mov_id)
    },
  },
  created() {
    this.getRecommend()
  },
}
/* 
<div
      style="
        display: grid;
        grid-auto-flow: column;
        grid-auto-columns: 23%;
        gap: var(--size-3);
        overflow-x: auto;
        overscroll-behavior-inline: contain;
        scroll-snap-type: inline mandatory;
        scroll-padding-inline: 5%;
      "
    >
      <img
        v-for="(movie, idx) in recommendMovies"
        :key="`rec-mov-sam-${idx}`"
        :id="`recmov-${idx}`"
        :src="`https://image.tmdb.org/t/p/original${movie?.poster_path}`"
        style="
          height: 100%;
          width: 100%;
          padding: 10px 10px 10px 10px;
          border-radius: 8px;
          object-fit: cover;
          scroll-snap-align: start;
        "
        @click="pushMovieDetail(movie.id)"
      />
    </div>
*/
</script>

<style>
/* .swiper-slide {
  width: 60%;
}

.swiper-slide:nth-child(2n) {
  width: 40%;
}

.swiper-slide:nth-child(3n) {
  width: 20%;
} 
  */
.collection-img-hov:hover {
  transform: scale(1.05);
  transition: all 0.2s;
  z-index: 10;
}
</style>
