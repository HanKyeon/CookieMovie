<template>
  <div id="article-form">
    <form @submit.prevent="postArticle" class="d-flex flex-column">
      <b-form-input
        v-model="inputTitle"
        class="my-3 form-control"
        size="lg"
        placeholder="제목을 입력하세요."
        style="background-color: transparent"
      ></b-form-input>
      <!-- <b-form-checkbox v-model="spoiler" class="form-control"
          >스포일러가 있는 게시글이에요!</b-form-checkbox
        > -->
      <b-form-textarea
        v-model="text"
        placeholder="게시글 내용을 입력하세요."
        class="form-control"
        v-model.trim="inputContent"
        rows="7"
        style="background-color: transparent"
      ></b-form-textarea>
      <button>작성하기</button>
    </form>
  </div>
</template>

<script>
//:src="`https://image.tmdb.org/t/p/original${article.movie.poster_path}`"
import axios from "axios"

export default {
  components: {},
  name: "ArticleForm",
  props: {},
  data() {
    return {
      spoiler: false,
      inputTitle: "",
      inputContent: "",
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
    postArticle() {
      if (!this.inputTitle || !this.inputContent) {
        alert("알맞은 데이터를 입력해주세요!")
      } else {
        axios({
          method: "post",
          url: `http://127.0.0.1:8000/community/article_list/${this.$route.params.movie_id}/`,
          headers: {
            Authorization: this.$store.state.token,
          },
          data: {
            spoiler: false, // default = false
            title: this.inputTitle,
            content: this.inputContent,
            // article_img: "", // 파일 경로가 아니라 문제.
          },
        })
          .then((res) => {
            this.spoiler = false
            this.inputTitle = ""
            this.inputContent = ""
            return res
          })
          .then((res) => {
            this.$router.push({
              name: "article",
              params: { article_id: res.data.id },
            })
            this.$emit("article-post")
          })
          .catch((err) => {
            alert("알맞은 데이터를 입력해주세요!")
            console.log(err)
          })
      }
    },
  },
}
</script>

<style>
#article-form {
  margin: auto;
  width: 80%;
  height: 40%;
}
#article-form .form-control {
  color: #e7e9f5;
}
</style>
