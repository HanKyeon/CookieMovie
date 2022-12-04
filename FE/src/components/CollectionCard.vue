<template>
  <div class="m-3">
    <h1>{{ collection.title }}</h1>
    <swiper class="swiper" :options="swiperOption">
      <swiper-slide
        v-for="(movie, idx) in collection?.movies"
        :key="`search-mov-${idx}`"
        :id="`search-${idx}`"
        style="height: 20%; width: 80%"
        :class="idx === 0 ? ['mx-3'] : ['mr-3']"
        class="p-2"
      >
        <img
          :src="`https://image.tmdb.org/t/p/original${movie?.poster_path}`"
          style="width: 100%; height: 100%"
          @click="pushMovieDetail(movie.id)"
          class="collection-img-hov"
        />
        <hr />
      </swiper-slide>
    </swiper>
  </div>
</template>

<script>
import { Swiper, SwiperSlide } from "vue-awesome-swiper"
import "swiper/css/swiper.css"

export default {
  name: "CollectionCard",
  components: {
    Swiper,
    SwiperSlide,
  },
  props: {
    collection: Object,
  },
  data() {
    return {
      swiperOption: {
        slidesPerView: 6,
        spaceBetween: 30,
        centeredSlides: false,
      },
    }
  },
  computed: {
    poster() {
      return {
        "--poster-Img": `url(https://image.tmdb.org/t/p/original${this.article.movie?.backdrop_path})`,
      }
    },
  },
  methods: {
    pushMovieDetail(mov_id) {
      this.$store.dispatch("pushMovieDetail", mov_id)
    },
  },
  updated() {
    let evt = document.createEvent("HTMLEvents")
    evt.initEvent("resize", true, false)
    window.dispatchEvent(evt)
  },
}
</script>

<style>
.collection-img-hov:hover {
  transform: scale(1.05);
  transition: all 0.2s;
  z-index: 10;
}
</style>
