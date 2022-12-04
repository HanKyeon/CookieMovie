<template>
  <div id="review-card" class="d-flex flex-column p-3 mt-3 mx-3 mb-0 pb-0">
    <div class="user-info d-flex justify-content-between">
      <div class="d-flex">
        <v-icon size="40" class="me-1">mdi-account-circle-outline</v-icon>

        <div
          class="d-flex flex-column justify-content-center"
          style="font-size: 0.7rem"
        >
          <span>{{ review.writer.username }}</span>
          <span>
            <v-icon small color="warning"> mdi-star </v-icon
            ><span>{{ review.score }}</span>
          </span>
        </div>
      </div>
      <div style="align-self: center">
        <!-- <v-icon @click="likeReview" :style="display:"> mdi-thumb-up-outline </v-icon> -->
        <v-icon id="thumb-icon" @click="likeReview">
          {{ is_liked ? "mdi-thumb-up" : "mdi-thumb-up-outline" }}</v-icon
        >
      </div>
    </div>
    <br />
    <!-- <v-divider></v-divider> -->
    <p style="font-weight: 900; text-align: left">
      {{ review.content }}{{ review.content }}{{ review.content
      }}{{ review.content }}{{ review.content }}
    </p>
    <v-divider></v-divider>
  </div>
</template>

<script>
//:src="`https://image.tmdb.org/t/p/original${article.movie.poster_path}`"
import axios from "axios"
export default {
  name: "ReviewCard",
  props: {
    review: Object,
  },
  data() {
    return {
      like_count: null,
      is_liked: false,
    }
  },
  computed: {
    poster() {
      return {
        "--poster-Img": `url(https://image.tmdb.org/t/p/original${this.review?.movie?.backdrop_path})`,
      }
    },
  },
  methods: {
    likeReview() {
      axios({
        method: "post",
        url: `http://127.0.0.1:8000/community/review_like/${this.review?.id}/`,
        headers: {
          Authorization: this.$store.state.token,
        },
        data: {},
      }).then((res) => {
        // const thumbIcon = document.getElementById("thumb-icon")
        if (res.data.is_liked) {
          this.like_count += 1
          this.is_liked = true
          // thumbIcon.innerText = "mdi-thumb-up"
        } else {
          this.like_count -= 1
          this.is_liked = false
          // thumbIcon.innerText = "mdi-thumb-up-outline"
        }
      })
    },
  },
  created() {
    this.like_count = this.review.like_count
    if (
      this.review.like_users.some((usr) => {
        return usr.username === this.$store.state.username
      })
    ) {
      this.is_liked = "true"
    } else {
      this.is_liked = "false"
    }
  },
  updated() {
    this.like_users = this.review.like_users.length
  },
}
</script>

<style>
#review-card {
  width: 100%;
  /* background-color: rgba(252, 244, 244, 0.2) !important; */
  color: rgba(0, 0, 0);
  /* backdrop-filter: brightness(100%); */
}
#review-card .v-icon {
  color: rgba(0, 0, 0, 0.74);
}
#review-card .v-divider {
}
</style>
