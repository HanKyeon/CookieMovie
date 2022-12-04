<template>
  <div id="pheed-card">
    <div class="info_section">
      <div class="user-info">
        <div>
          <b-avatar
            variant=""
            :src="`http://127.0.0.1:8000/static/default_img/ndg.png`"
          ></b-avatar
          ><span @click="pushUserDetail(article.writer.username)">{{
            article.writer.username
          }}</span>
        </div>
        <small>4분 전</small>
      </div>
      <div class="article-info">
        <b-card-text class="" v-text="article.content"> </b-card-text>
        <b-button
          pill
          class="bg-indigo border-0"
          @click.prevent="pushArticleDetail(article.id)"
          >더보기</b-button
        >
      </div>
      <div class="social-info">
        <span>좋아요 {{ article.like_count }}</span
        ><br />
        <span>댓글 {{ article.comment_count }}</span>
        <h1>{{ backdrop }}</h1>
      </div>
    </div>
    <div class="img" :style="poster" />
  </div>
</template>

<script>
//:src="`https://image.tmdb.org/t/p/original${article.movie.poster_path}`"
export default {
  name: "PheedCard",
  props: {
    article: Object,
  },
  computed: {
    poster() {
      return {
        "--poster-Img": `url(https://image.tmdb.org/t/p/original${this.article.movie?.backdrop_path})`,
      }
    },
  },
  methods: {
    pushUserDetail(usnm) {
      this.$store.dispatch("pushUserDetail", usnm)
    },
    pushArticleDetail(arid) {
      this.$router.push({ name: "article", params: { article_id: arid } })
    },
  },
}
</script>

<style>
#pheed-card {
  position: relative;
  display: block;
  width: 800px;
  height: auto;
  margin: 80px auto;
  overflow: hidden;
  border-radius: 10px;
  transition: all 0.4s;
  box-shadow: 0px 0px 120px -25px rgba(0, 0, 0, 1);
  color: black;
}
#pheed-card:hover {
  transform: scale(1.02);
  box-shadow: 0px 0px 80px -25px rgba(0, 0, 0, 1);
  transition: all 0.4s;
}
#pheed-card .info_section {
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
#pheed-card .info_section .user-info {
  position: relative;
  padding-top: 20px;
  padding-left: 20px;
  width: 50%;
  text-align: left;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
#pheed-card .info_section .user-info small {
  color: gray;
}
#pheed-card .info_section .article-info {
  position: relative;
  padding-top: 10px;
  padding-left: 25px;
  height: 60%;
  width: 50%;
}
#pheed-card .info_section .article-info .card-text {
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
#pheed-card .info_section .article-info .show-all {
  display: block;
  overflow: visible;
}
#pheed-card .btn {
  float: right;
  font-size: 0.5rem;
  padding: 2% 3% 1%;
}

#pheed-card .info_section .social-info {
  position: relative;
  width: 50%;
  text-align: right;
  font-size: 0.8rem;
  margin-block: 3%;
  flex: 1 1 auto;
  display: flex;
  justify-content: end;
}
#pheed-card .info_section .social-info span {
  margin-left: 5%;
}

#pheed-card .img {
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
}

/* @media screen and (min-width: 768px) {
  #pheed-card .movie_header {
    width: 65%;
  }

  #pheed-card .movie_desc {
    width: 50%;
  }

  #pheed-card .info_section {
   background: linear-gradient(to right, #ffffffc4 50%, transparent 100%);
  }

  #pheed-card .blur_back {
    width: 80%;
    background-position: -100% 10% !important;
  }
} */
/* @media screen and (max-width: 768px) {
    #pheed-card {
      width: 95%;
      margin: 70px auto;
      min-height: 350px;
      height: auto;
    }

    #pheed-card .blur_back {
      width: 100%;
      background-position: 50% 50% !important;
    }

    #pheed-card .movie_header {
      width: 100%;
      margin-top: 85px;
    }

    #pheed-card .movie_desc {
      width: 100%;
    }

    #pheed-card .info_section {
      background: linear-gradient(to top, #0a0a0a7a 50%, transparent 100%);
      display: inline-grid;
    }
  } */
</style>
