<template>
  <v-sheet id="review-form" class="p-4" rounded>
    <v-form ref="form" lazy-validation>
      <!-- :error-messages="contentErrors" -->
      <div class="d-flex justify-content-around">
        <div class="d-flex flex-column me-5">
          <v-rating
            background-color="grey lighten-1"
            color="warning"
            half-increments
            hover
            length="5"
            size="35"
            v-model="score"
            icon-label="custom icon label text {0} of {1}"
          ></v-rating>
          <v-select
            v-model="selected"
            :items="options"
            item-text="text"
            item-value="value"
            label="어떤 점이 좋은지 알려주세요!"
            persistent-hint
            outlined
            required
            class="mt-3"
            color="blue darken-4"
          >
          </v-select>
          <v-checkbox
            v-model="spoiler"
            label="스포일러가 있나요?"
            dense
            class="m-0"
            color="green"
          ></v-checkbox>
        </div>
        <v-textarea
          style="width: 60%"
          :rules="rules"
          counter
          maxlength="200"
          hint="최대 200자까지 작성할 수 있어요."
          name="content"
          auto-grow
          full-width
          v-model="inputContent"
          label="리뷰를 남겨주세요."
          required
          solo
          filled
          rows="5"
          row-height="30"
        ></v-textarea>
      </div>

      <!-- :error-messages="selectErrors" -->

      <v-btn class="mr-4" @click="postReview"> submit </v-btn>
      <v-btn @click="clear"> clear </v-btn>
    </v-form>
  </v-sheet>
</template>

<script>
//:src="`https://image.tmdb.org/t/p/original${article.movie.poster_path}`"
import axios from "axios"
// import RatingComponent from "./RatingComponent.vue"

export default {
  // components: { RatingComponent },
  name: "ReviewForm",
  props: {},
  data() {
    return {
      rules: [(v) => v.length <= 200 || "Max 200 characters"],
      spoiler: false,
      inputContent: "",
      score: 0,
      selected: null,
      options: [
        {
          value: 1,
          text: "음악이 좋은",
        },
        {
          value: 2,
          text: "영상이 아름다운",
        },
        {
          value: 3,
          text: "흡입력이 강한",
        },
        {
          value: 4,
          text: "액션이 통쾌한",
        },
        {
          value: 5,
          text: "여운이 남는",
        },
        {
          value: 6,
          text: "인생 최고의",
        },
        {
          value: 7,
          text: "연기력이 뛰어난",
        },
        {
          value: 8,
          text: "스토리가 흥미로운",
        },
        {
          value: 9,
          text: "꼭 영화관 가서 봐야하는",
        },
        {
          value: 10,
          text: "가슴 설레는",
        },
        {
          value: 11,
          text: "눈물이 흐르는",
        },
        {
          value: 12,
          text: "손에 땀을 쥐게 하는",
        },
        {
          value: 13,
          text: "가족과 보기 좋은",
        },
        {
          value: 14,
          text: "연인과 함께하기 좋은",
        },
        {
          value: 15,
          text: "혼자 보기 좋은",
        },
      ],
    }
  },
  computed: {
    movieID() {
      return parseInt(this.$route.params.movie_id)
    },
    // selectErrors() {
    //   const errors = []
    //   // if (!this.select.$dirty) return errors
    //   !this.select.required && errors.push("Item is required")
    //   return errors
    // },
    // contentErrors() {
    //   const errors = []
    //   // if (!this.inputContent.$dirty) return errors
    //   !this.inputContent.required && errors.push("Content is required.")
    //   return errors
    // },
  },
  methods: {
    postReview() {
      if (!this.selected === null || !this.inputContent) {
        console.log("hi")
      } else {
        axios({
          method: "post",
          url: `http://127.0.0.1:8000/community/review_list/${this.movieID}/`,
          headers: {
            Authorization: this.$store.state.token,
          },
          data: {
            spoiler: this.spoiler, // default = false
            score: this.score,
            content: this.inputContent,
            topic: this.selected,
            // review_img: "", // 파일 경로가 아니라 문제.
          },
        })
          .then((res) => {
            this.spoiler = false
            this.score = 0
            this.inputContent = ""
            this.selected = null
            console.log(res)
            this.$emit("review-post")
          })
          .catch((err) => {
            alert("알맞은 데이터를 입력해주세요!")
            console.log(err)
          })
      }
    },
    clear() {
      this.inputContent = ""
      this.selected = null
    },
    scoreSet(emitScore) {
      this.score = emitScore
    },
  },
}
</script>

<style>
#review-form {
  background: rgba(255, 255, 255, 0.35);
  /* background: rgba(255, 255, 255, 0.459); */
  width: 100%;
}
</style>
