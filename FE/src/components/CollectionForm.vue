<template>
  <div style="width: 100vw; height: 80vh" class="black-bg" id="collection-form">
    <div class="container white-bg">
      <form @submit.prevent="postCollection">
        <b-form-input
          v-model="inputTitle"
          class="mb-3 form-control"
          size="lg"
          placeholder="컬렉션 제목을 입력하세요."
        ></b-form-input>

        <swiper class="swiper m-1" :options="swiperOption">
          <swiper-slide
            v-for="(movie, idx) in sellectedMovies"
            :key="`search-mov-${idx}`"
            :id="`search-${idx}`"
            :class="idx === 0 ? ['mx-3'] : ['mr-3']"
          >
            <img
              :src="`https://image.tmdb.org/t/p/original${movie?.poster_path}`"
              style="height: 100%; width: 100%"
              @click="toggleMovie(movie.id, movie.poster_path)"
              class="collection-img-hov p-2"
            />
          </swiper-slide>
        </swiper>

        <b-form-input
          v-model.trim="searchKeyword"
          class="my-3 form-control"
          size="lg"
          placeholder="검색어를 입력하세요."
        ></b-form-input>

        <swiper class="swiper m-1" :options="swiperOption">
          <swiper-slide
            v-for="(movie, idx) in searchMovieList"
            :key="`search-mov-${idx}`"
            :id="`search-${idx}`"
            class="p-2"
            :class="idx === 0 ? ['mx-3'] : ['mr-3']"
          >
            <img
              :src="`https://image.tmdb.org/t/p/original${movie?.poster_path}`"
              style="height: 100%; width: 100%"
              class="collection-img-hov p-1"
              @click="toggleMovie(movie.id, movie.poster_path)"
            />
          </swiper-slide>
        </swiper>

        <hr />
        <button type="submit" class="form-control" id="collection-submit">
          컬렉션 생성 완료
        </button>
      </form>
    </div>
  </div>
</template>

<script>
/* 
import { Swiper, SwiperSlide } from "vue-awesome-swiper"
import "swiper/css/swiper.css"

  components: {
    Swiper,
    SwiperSlide,
  },

<swiper class="swiper" :options="swiperOption">
  <swiper-slide
    v-for="(movie, idx) in searchMovieList"
    :key="`search-mov-${idx}`"
    :id="`search-${idx}`"
  >
    <img
      :src="`https://image.tmdb.org/t/p/original${movie?.poster_path}`"
      style="height: 100%; width: 100%"
      @click="toggleMovie(movie.id, movie.poster_path)"
    />
  </swiper-slide>
</swiper>

data() {
  return {
    swiperOption: {
      slidesPerView: 6,
      spaceBetween: 30,
      centeredSlides: false,
    },
  }
}

*/
import axios from "axios"
import { Swiper, SwiperSlide } from "vue-awesome-swiper"
import "swiper/css/swiper.css"

export default {
  components: {
    Swiper,
    SwiperSlide,
  },
  name: "CollectionForm",
  props: {},
  data() {
    return {
      spoiler: false,
      inputTitle: "",
      collectionList: [],
      searchKeyword: "",
      searchMovieList: [],
      sellectedMovies: [],
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
    movieID() {
      return parseInt(this.$route.params.movie_id)
    },
  },
  methods: {
    postCollection() {
      if (this.inputTitle === "" || this.collectionList.length === 0) {
        alert("데이터 잘 넣어주세여!")
      } else {
        axios({
          method: "post",
          url: `http://127.0.0.1:8000/movies/collection_list/`,
          headers: {
            Authorization: this.$store.state.token,
          },
          data: {
            title: this.inputTitle,
            movies: this.collectionList,
          },
        })
          .then((res) => {
            console.log(res)
            this.$store.dispatch("getUserData", this.$route.params.username)
            this.$emit("collection-add")
          })
          .catch((err) => {
            alert(err)
          })
      }
    },
    searchMovie(kw) {
      axios({
        method: "post",
        url: `http://127.0.0.1:8000/movies/search/`,
        headers: {},
        data: {
          searchKw: kw,
        },
      }).then((res) => {
        this.searchMovieList = res.data
      })
    },
    toggleMovie(mov_id, p_p) {
      if (
        this.collectionList.some((val) => {
          return val === mov_id
        })
      ) {
        this.collectionList = this.collectionList.filter((val) => {
          return val !== mov_id
        })
        this.sellectedMovies = this.sellectedMovies.filter((val) => {
          return val.id !== mov_id
        })
      } else {
        this.collectionList.push(mov_id)
        this.sellectedMovies.push({ id: mov_id, poster_path: p_p })
      }
      console.log(this.collectionList)
    },
  },
  watch: {
    searchKeyword(newValue, oldValue) {
      if (newValue) {
        this.searchMovie(newValue)
      } else {
        this.searchMovie(oldValue)
      }
    },
  },
}
</script>

<style>
.collection-img-hov:hover {
  transform: scale(1.05);
  transition: all 0.2s;
  z-index: 10;
}
#collection-form {
  margin: 0;
  z-index: 10;
  position: absolute;
}
div {
  box-sizing: border-box;
}

.black-bg {
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  padding: 20px;
}
.white-bg {
  width: 100%;
  height: 100%;
  background: white;
  border-radius: 8px;
  padding: 20px;
}
#collection-submit {
  color: black;
}
</style>
