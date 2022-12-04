<template>
  <div id="article-card">
    <v-card class="mx-auto w-100 h-100">
      <v-card-title>
        <v-icon large left> mdi-account-voice </v-icon>
        <span>{{ article?.title }}</span>
      </v-card-title>

      <v-card-text class="paragraph">
        {{ article?.content }}
      </v-card-text>

      <v-card-actions style="height: 18%">
        <v-list-item class="grow">
          <v-list-item-avatar color="grey darken-3">
            <v-img
              class="elevation-6"
              alt="profile-img"
              src="https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairShortCurly&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=White&eyeType=Default&eyebrowType=DefaultNatural&mouthType=Default&skinColor=Light"
            ></v-img>
          </v-list-item-avatar>

          <v-list-item-content>
            <v-list-item-title>{{
              article?.writer.username
            }}</v-list-item-title>
          </v-list-item-content>

          <v-row align="center" justify="end">
            <v-icon class="mr-1"> mdi-heart </v-icon>
            <span class="subheading mr-2">{{ article.like_count }}</span>
            <span class="mr-1">·</span>
            <v-icon class="mr-1"> mdi-comment-processing </v-icon>
            <span class="subheading">{{ article?.comment_count }}</span>
          </v-row>
        </v-list-item>
      </v-card-actions>
    </v-card>
    <!-- <div class="info_section">
      <div class="user-info">
        <div>
          <b-avatar
            variant=""
            :src="`http://127.0.0.1:8000/static/default_img/ndg.png`"
          ></b-avatar>
          <span>{{ article.writer.username }}</span>
        </div>
        <small>4분 전</small>
      </div>
      <div class="article-info">
        <b-card-text class=""
          >제목 : {{ article.title }} <br />{{ article.content }}</b-card-text
        >
        <b-button
          @click="pushArticle(article.id)"
          pill
          class="bg-indigo border-0"
          >더보기</b-button
        >
      </div>
      <hr />
      <div class="social-info">
        <span>좋아요 {{ article.like_count }}</span>
        <span>댓글 {{ article.comment_count }}</span>
        <span>{{ likeText }}</span>
        <h1>{{ backdrop }}</h1>
      </div>
    </div>
    <div class="img" :style="poster" /> -->
  </div>
</template>

<script>
//:src="`https://image.tmdb.org/t/p/original${article.movie.poster_path}`"
export default {
  name: "ArticleCard",
  props: {
    article: Object,
  },
  data() {
    return {
      likeText: "",
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
    pushArticle(article_id) {
      this.$router.push({ name: "article", params: { article_id: article_id } })
    },
  },
}
</script>

<style>
#article-card {
  height: 40vh;
  width: 17vw;
  /* overflow: auto; */
  /* position: relative;
  display: block;
  width: 800px;
  height: auto;
  margin: 80px auto;
  overflow: hidden; */
  /* border-radius: 10px;
  transition: all 0.4s;
  box-shadow: 0px 0px 120px -25px rgba(0, 0, 0, 1);
  color: black; */
}
#article-card .v-card__title {
  height: 17%;
  /* font-weight: bold; */
}
#article-card .v-card__text {
  overflow: auto;
  height: 65%;
  padding: 1rem 2rem;
}
/* #article-card:hover {
  transform: scale(1.02);
  box-shadow: 0px 0px 80px -25px rgba(0, 0, 0, 1);
  transition: all 0.4s;
}
#article-card .info_section {
  position: relative;
  width: 100%;
  height: 100%;
  padding: 1% 2%;
  text-align: left;
  z-index: 2;
  border-radius: 10px;
  background: linear-gradient(
    to right,
    rgb(30, 30, 30),
    rgb(35, 35, 35),
    rgb(51, 49, 49) 28%,
    transparent 100%
  );
  display: flex;
  flex-direction: column;
  color: white;
}
#article-card .info_section .user-info {
  position: relative;
  padding-top: 20px;
  padding-left: 20px;
  width: 50%;
  text-align: left;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
#article-card .info_section .user-info small {
  color: gray;
}
#article-card .info_section .article-info {
  position: relative;
  padding-top: 10px;
  padding-left: 25px;
  height: 60%;
  width: 50%;
}
#article-card .info_section .article-info .card-text {
  display: -webkit-box;
  -webkit-line-clamp: 5;
  -webkit-box-orient: vertical;
  width: 360px;
  height: 100%;
  overflow: hidden;
  text-overflow: ellipsis;
  line-height: 170%;
  font-size: 0.95rem;
}
#article-card .info_section .article-info .show-all {
  display: block;
  overflow: visible;
}
#article-card .btn {
  float: right;
  font-size: 0.5rem;
  padding: 2% 3% 1%;
}

#article-card .info_section .social-info {
  position: relative;
  width: 50%;
  text-align: right;
  font-size: 0.8rem;
  margin-block: 3%;
  flex: 1 1 auto;
  display: flex;
  justify-content: end;
}
#article-card .info_section .social-info span {
  margin-left: 5%;
}

#article-card .img {
  width: 80%;
  height: 100%;
  position: absolute;
  top: 0;
  right: 0;
  z-index: 1;
  background: var(--poster-Img);
  background-size: contain;
  background-repeat: no-repeat;
  background-position: right top;
  border-radius: 11px;
} */

/* @media screen and (min-width: 768px) {
  #article-card .movie_header {
    width: 65%;
  }

  #article-card .movie_desc {
    width: 50%;
  }

  #article-card .info_section {
   background: linear-gradient(to right, #ffffffc4 50%, transparent 100%);
  }

  #article-card .blur_back {
    width: 80%;
    background-position: -100% 10% !important;
  }
} */
/* @media screen and (max-width: 768px) {
    #article-card {
      width: 95%;
      margin: 70px auto;
      min-height: 350px;
      height: auto;
    }

    #article-card .blur_back {
      width: 100%;
      background-position: 50% 50% !important;
    }

    #article-card .movie_header {
      width: 100%;
      margin-top: 85px;
    }

    #article-card .movie_desc {
      width: 100%;
    }

    #article-card .info_section {
      background: linear-gradient(to top, #0a0a0a7a 50%, transparent 100%);
      display: inline-grid;
    }
  } */
</style>
