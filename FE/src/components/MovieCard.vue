<template>
  <div class="card flex-row" :class="flag ? ['open'] : ['']">
    <img
      :src="`https://image.tmdb.org/t/p/original/${movie?.poster_path}`"
      class="movie-poster-all"
      @click.prevent="pushMovieDetail"
    />
    <div class="flex-column info">
      <div
        class="title"
        style="cursor: pointer"
        @click.prevent="pushMovieDetail"
      >
        {{ movie?.title }}
      </div>
      <div
        class="author"
        style="cursor: pointer; font-weight: normal"
        @click.prevent="pushMovieDetail"
      >
        {{ movie?.original_title }}
      </div>
      <button @click="toggleOpen" style="font-weight: normal">
        {{ btnText }}
      </button>
      <div class="bottom summary">
        {{ movie?.overview }}
      </div>
    </div>
    <second-review-form
      v-show="flag && !reviewFlag"
      class="flex-column maybe-review justify-content-center align-items-between"
      style="width: 23%; height: 100%"
      @review-post="reviewPost"
      :movieID="movie.id"
      :myReview="myReview"
    />
    <div v-if="flag && reviewFlag" style="width: 23%; height: 100%">
      <h3>리뷰를 이미 남기셨습니다!</h3>
      <img
        :src="`http://127.0.0.1:8000/static/WordCloud/movie${movie?.id}.png`"
        style="width: 100%; height: 73%"
      />
    </div>
  </div>
</template>

<script>
import SecondReviewForm from "./SecondReviewForm.vue"
import axios from "axios"
export default {
  components: { SecondReviewForm },
  name: "MovieCard",
  props: {
    movie: Object,
  },
  data() {
    return {
      flag: false,
      movieReviews: [],
      reviewFlag: false,
    }
  },
  computed: {
    myReview() {
      let reviews = this.movieReviews
      let review = reviews.find((val) => {
        return val.writer === this.$store.state.userData.id
      })
      return review
    },
    btnText() {
      let ret
      if (this.reviewFlag) {
        ret = "Check Review Data"
      } else {
        ret = "Write Review"
      }
      return ret
    },
  },
  methods: {
    toggleOpen() {
      this.flag = !this.flag
    },
    pushMovieDetail() {
      this.$store.dispatch("pushMovieDetail", this.movie.id)
    },
    setReviewFlag() {
      this.reviewFlag = this.movieReviews.find((val) => {
        return val.writer === this.$store.state.userData.id
      })
    },
    reviewPost() {
      this.getReviews()
    },
    getReviews() {
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/community/review_list/${this.movie.id}/`,
        headers: {},
        data: {},
      }).then((res) => {
        this.movieReviews = res.data
        this.setReviewFlag()
      })
    },
  },
  watch: {},
  mounted() {
    // let a = document.querySelectorAll(".card")
    // a.forEach((val) => {
    //   val.addEventListener("click", (e) => {
    //     e.preventDefault()
    //     val.classList.toggle("open")
    //   })
    // })
  },
  created() {
    this.getReviews()
  },
}
</script>

<style></style>
