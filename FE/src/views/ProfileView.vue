<template>
  <b-row id="profile">
    <b-col cols="3">
      <div
        class="d-flex align-self-center justify-content-center"
        style="
          border-radius: 50%;
          background-color: lightsteelblue;
          box-shadow: 0 0 10px 3px;
          margin: 10% 25%;
        "
      >
        <img
          id="logo"
          :src="`http://127.0.0.1:8000/static/default_img/ndg.png`"
        />
      </div>
      <h1>{{ username }}</h1>
      <p>
        {{ userData?.user_msg ? userData.user_msg : "한 줄 소개가 없습니다." }}
      </p>
    </b-col>
    <b-col cols="9" class="px-5">
      <div>
        <b-tabs content-class="mt-3" justified>
          <b-tab title="Ticket Book" active>
            <ticket-book :reviews="reviews" />
          </b-tab>
          <b-tab title="Collections" style="width: 95%">
            <button
              class="m-3 form-control"
              style="width: 100%"
              @click.prevent="changeCollectionFlag"
            >
              {{ collectionBtnText }}
            </button>
            <collection-form
              v-if="collectionFlag"
              @collection-add="changeCollectionFlag"
              style="width: 95%; height: auto"
            />
            <collection-card
              v-for="(collection, idx) in collections"
              :key="`collection-profile-${idx}`"
              :collection="collection"
              style="height: 80%, width: 20%"
            />
          </b-tab>
          <b-tab title="Community History">
            <b-container fluid>
              <p>내가 작성한 글</p>
              <b-row>
                <article-card
                  v-for="(article, idx) in articles"
                  :key="`article-profile-${idx}`"
                  :article="article"
                />
              </b-row>
              <b-row>내가 남긴 리뷰</b-row>
              <review-card
                v-for="(review, idx) in reviews"
                :key="`review-profile-${idx}`"
                :review="review"
              />
            </b-container>
          </b-tab>
          <b-tab title="Edit Profile">
            <printing-ticket />
          </b-tab>
        </b-tabs>
      </div>
    </b-col>
    <!-- <moving-ticket style="width: 40%; height: 10%" /> -->
    <!-- <ticket-item /> -->
    <br />
    <br />
    <!-- <hr-ticket /> -->
  </b-row>
</template>

<script>
// import MovieRecommendations from "../components/MovieRecommendations.vue"
import PrintingTicket from "../components/PrintingTicket.vue"
// import HrTicket from "../components/hrTicket.vue";
import TicketBook from "../components/TicketBook.vue"
import axios from "axios"
import ArticleCard from "@/components/ArticleCard.vue"
import ReviewCard from "@/components/ReviewCard.vue"
import CollectionCard from "@/components/CollectionCard.vue"
import CollectionForm from "@/components/CollectionForm.vue"
// import TicketItem from "../components/TicketItem.vue";
// @ is an alias to /src

export default {
  components: {
    TicketBook,
    // MovieRecommendations,
    PrintingTicket,
    ArticleCard,
    ReviewCard,
    CollectionCard,
    CollectionForm,
  },
  name: "ProfileView",
  data() {
    return {
      username: null,
      userData: null,
      collectionFlag: false,
    }
  },
  computed: {
    routeUsername() {
      return this.$router.params.username
    },
    reviews() {
      if (this.userData) {
        let a = this.userData.reviews
        a.reverse()
        return a
      } else {
        return null
      }
    },
    articles() {
      if (this.userData) {
        let a = this.userData.articles
        a.reverse()
        return a
      } else {
        return null
      }
    },
    collections() {
      if (this.userData) {
        let a = this.userData.collections
        a.reverse()
        return a
      } else {
        return null
      }
    },
    collectionBtnText() {
      if (this.collectionFlag) {
        return "닫기"
      } else {
        return "컬렉션 만들기"
      }
    },
  },
  methods: {
    getUser() {
      this.username = this.$route.params.username
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/accounts/detail/${this.username}/`,
        headers: {},
        data: {},
      }).then((res) => {
        this.userData = res.data
      })
    },
    changeCollectionFlag() {
      this.collectionFlag = !this.collectionFlag
      this.getUser()
    },
  },
  watch: {
    routeUsername() {
      this.getUser()
    },
  },
  created() {
    this.getUser()
    var evt = document.createEvent("HTMLEvents")
    evt.initEvent("resize", true, false)
    window.dispatchEvent(evt)
  },
}
</script>
