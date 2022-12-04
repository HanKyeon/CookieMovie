<template>
  <main id="hr-ticket">
    <div class="ticket-wrapper">
      <div class="ticket left">
        <div class="d-flex justify-content-between align-items-start">
          <h3 class="text-left">MOVIE TITLE</h3>
          <span>리뷰 : {{ review }}</span>
        </div>

        <rating-component />

        <div class="review mt-3">
          <h6>{{ review }}</h6>
          <span
            >이것은 짧은 리뷰입니다.이것은 짧은 리뷰입니다.이것은 짧은
            리뷰입니다.이것은 짧은 리뷰입니다.이것은 짧은 리뷰입니다.이것은 짧은
            리뷰입니다</span
          >
        </div>
      </div>
      <div class="ticket right">
        <div class="stamp">
          <!-- <span>Date</span> -->
          <span>22-11-19</span>
        </div>
        <!-- <img
          src="https://www.themoviedb.org/t/p/w600_and_h900_bestv2/eTOqjSNjMUpnjbRCnYElU4b5uWW.jpg"
          alt=""
          class="poster"
        /> -->
      </div>
    </div>
  </main>
</template>

<script>
import RatingComponent from "./RatingComponent.vue"
export default {
  name: "TicketItem",
  components: {
    RatingComponent,
  },
  props: {
    review: Object,
  },
}
</script>

<style>
/* @import url("https://fonts.googleapis.com/css2?family=Yanone+Kaffeesatz:wght@300;400;500;600;700&display=swap"); */
#hr-ticket {
  max-width: 40%;
  color: black;
  /* transform: rotate(270deg); */
  /* font-family: "Yanone Kaffeesatz"; */
}

#hr-ticket .ticket-wrapper {
  padding-bottom: 10px;
  /* width: 35em;
  height: 20em; */
  display: flex;
  align-items: center;
  /* flex-direction: column; */
  /* flex-shrink: 1; */
}
#hr-ticket .ticket.left {
  width: 75%;
  height: 30%;
  display: flex;
  flex-direction: column;
}

#hr-ticket .ticket.left .review {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  width: 285px;
  height: 100%;
  overflow: hidden;
  text-overflow: ellipsis;
  font-size: 0.5em;
  line-height: 150%;
}
#hr-ticket .poster {
  max-width: 100%;
  max-height: 100%;
  /* flex-shrink: 1; */
  /* transform: rotate(90deg); */
  object-fit: cover;
}

#hr-ticket .ticket {
  padding: 25px 30px;
  text-align: left;
  min-height: 200px;
  /* width: 88%; */
  background-color: #fff;
  border-radius: 10px 10px 20px 20px;
  box-shadow: 1px 3px 8px 3px rgba(0, 0, 0, 0.5);
}

#hr-ticket .ticket.right {
  /* height: 110px; */
  height: 30%;
  width: 25%;
  padding-inline: 0.8%;
  position: relative;
  border-radius: 20px 20px 10px 10px;
  /* display: flex;
  align-items: flex-start; */
  font-size: 2vw;
  background-image: url("https://www.themoviedb.org/t/p/w600_and_h900_bestv2/eTOqjSNjMUpnjbRCnYElU4b5uWW.jpg");
  background-size: contain;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 1em;
}
#hr-ticket .ticket.right::before {
  content: "";
  background: linear-gradient(to bottom, #fff 50%, #359fcf 50%);
  background-size: 22px 4px, 100% 4px;
  height: 88%;
  width: 4px;
  display: block;
  left: -1.3%;
  top: 6.5%;
  border-radius: 25%;
  position: absolute;
  margin: auto;
}
#hr-ticket .ticket.right .stamp {
  border: 3px solid #fff;
  border-radius: 10%;
  transform: rotate(-20deg);
  color: #fff;
  padding: 3% 5%;
  font-size: 1em;
  font-weight: bold;
  -webkit-mask-image: url("https://s3-us-west-2.amazonaws.com/s.cdpn.io/8399/grunge.png");
  -webkit-mask-size: 944px 604px;
  mix-blend-mode: plus-lighter;
  backdrop-filter: blur(5px);
}
</style>
