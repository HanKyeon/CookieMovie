<template>
  <div id="article-form">
    <form @submit.prevent="postComment" class="d-flex flex-column">
      <!-- <b-form-checkbox v-model="spoiler" class="form-control"
          >스포일러가 있는 게시글이에요!</b-form-checkbox
        > -->
      <h3>댓글 작성</h3>
      <b-form-textarea
        v-model="text"
        placeholder="게시글 내용을 입력하세요."
        class="form-control"
        v-model.trim="inputContent"
        rows="3"
        style="background-color: transparent"
      ></b-form-textarea>
      <button>댓글 작성 완료</button>
    </form>
  </div>
</template>

<script>
//:src="`https://image.tmdb.org/t/p/original${article.movie.poster_path}`"
import axios from "axios"

export default {
  components: {},
  name: "CommentForm",
  props: {},
  data() {
    return {
      spoiler: false,
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
    postComment() {
      if (!this.inputContent) {
        alert("알맞은 데이터를 입력해주세요!")
      } else {
        axios({
          method: "post",
          url: `http://127.0.0.1:8000/community/comment_list/${this.$route.params.article_id}/`,
          headers: {
            Authorization: this.$store.state.token,
          },
          data: {
            spoiler: false,
            content: this.inputContent,
            // comment_img: "a.jpg", // 확장자 명으로도 안되는거 같은데... 머지 ㅜ
          },
        })
          .then((res) => {
            this.spoiler = false
            this.inputContent = ""
            this.$emit("post-comment", res)
          })
          .catch((err) => {
            alert(err)
          })
      }
    },
  },
}
</script>

<style>
#article-form {
  margin: 0;
  width: 80%;
  height: 40%;
  /* backdrop-filter: opacity(0.5); */
  /* z-index: 10; */
  /* position: absolute; */
}
#article-form .form-control {
  color: #e7e9f5;
}
/* .black-bg {
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  padding: 20px;
} */
/* .white-bg {
  width: 100%;
  height: 100%;
  background: white;
  border-radius: 8px;
  padding: 20px;
} */
</style>
