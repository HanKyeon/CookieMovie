<template>
  <div>
    <div
      id="article"
      style="
        height: auto;
        width: 93.3%;
        border-radius: 50px;
        background: lightgrey;
      "
      class="p-3 m-5"
    >
      <br />
      <br />
      <h1 style="color: black">{{ article.title }}</h1>
      <br />
      <div class="px-5 pb-5" style="">
        <h5 style="color: black">{{ article.content }}</h5>
      </div>
      <div class="d-flex flex-row justify-content-between">
        <span>좋아요 갯수 : {{ article.like_count }}</span>
        <span>댓글 갯수 : {{ article.comment_count }}</span>
      </div>
      <div
        v-for="(comment, idx) in article.comments"
        :key="`article-comment-${idx}`"
      >
        <br />
        <div
          style="
            height: auto;
            width: 100%;
            background: white;
            border-radius: 10px;
          "
        >
          <div
            style="
              background: rgba(21, 21, 21, 0.3);
              border-radius: 10px;
              height: auto;
            "
            class="p-3 d-flex"
          >
            <div class="d-flex flex-row justify-content-between">
              <span>작성자 : {{ comment.writer.username }}</span>
              <v-btn
                fab
                small
                @click="commentLike(comment.id)"
                :style="{ color: heartColor }"
              >
                <v-icon>mdi-heart</v-icon>
              </v-btn>
              <span>|좋아요 : {{ comment.like_count }}개</span>
            </div>
            |
            <div>댓글 내용 : {{ comment.content }}</div>
          </div>
        </div>
      </div>
      <br />
      <comment-form
        style="
          background: rgba(21, 21, 21, 0.2);
          border-radius: 12px;
          width: 100%;
        "
        class="p-3"
        @post-comment="getArticle"
      />
      <br />
    </div>
  </div>
</template>

<script>
import axios from "axios"
import CommentForm from "../components/CommentForm.vue"
// @ is an alias to /src

export default {
  components: { CommentForm },
  name: "ArticleView",
  data() {
    return {
      article: null,
    }
  },
  methods: {
    getArticle() {
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/community/article_detail/${this.$route.params.article_id}/`,
        headers: {},
        data: {},
      }).then((res) => {
        this.article = res.data
      })
    },
    commentLike(com_id) {
      axios({
        method: "post",
        url: `http://127.0.0.1:8000/community/comment_like/${com_id}/`,
        headers: {
          Authorization: this.$store.state.token,
        },
        data: {},
      }).then((res) => {
        console.log(res)
        this.getArticle()
      })
    },
  },
  created() {
    this.getArticle()
  },
}
</script>
