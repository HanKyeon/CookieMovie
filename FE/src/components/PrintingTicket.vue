<template>
  <!-- INSPO:  https://www.behance.net/gallery/69583099/Mobile-Flights-App-Concept -->
  <main class="ticket-system">
    <div class="top">
      <h1 class="title">티켓 발급 중...</h1>
      <div class="printer" />
    </div>
    <div class="receipts-wrapper">
      <div class="receipts">
        <div class="receipt">
          <span>No. 187</span>
          <h2 class="text-right">Movie Title</h2>
          <img
            src="https://www.themoviedb.org/t/p/w600_and_h900_bestv2/eTOqjSNjMUpnjbRCnYElU4b5uWW.jpg"
            alt=""
            class="poster"
          />
          <div class="details">
            <div class="item">
              <h6>Date</h6>
              <span>2022/11/22</span>
            </div>
            <div class="item">
              <h6>Rate</h6>
              <rating-component />
            </div>
          </div>
        </div>
        <div class="receipt bottom">
          <div class="item">
            <h6>Review</h6>
            <span
              >이것은 짧은 리뷰입니다.이것은 짧은 리뷰입니다.이것은 짧은
              리뷰입니다.이것은 짧은 리뷰입니다</span
            >
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import RatingComponent from "./RatingComponent.vue";
export default {
  name: "PrintingTicket",
  components: {
    RatingComponent,
  },
};
</script>

<style>
.ticket-system {
  max-width: 30%;
  /* max-width: 385px; */
  color: black;
}

.ticket-system .poster {
  max-width: 100%;
}
.ticket-system .top {
  display: flex;
  align-items: center;
  flex-direction: column;
}
.ticket-system .top .title {
  font-weight: normal;
  font-size: 1.6rem;
  text-align: left;
  /* margin-left: 20px; */
  margin-bottom: 30px;
  color: #fff;
}
.ticket-system .top .printer {
  width: 90%;
  height: 20px;
  border: 5px solid #fff;
  border-radius: 10px;
  box-shadow: 1px 3px 3px 0px rgba(0, 0, 0, 0.2);
}
.ticket-system .receipts-wrapper {
  overflow: hidden;
  margin-top: -10px;
  padding-bottom: 10px;
}
.ticket-system .receipts {
  width: 100%;
  display: flex;
  align-items: center;
  flex-direction: column;
  transform: translateY(-510px);
  animation-duration: 2.5s;
  animation-delay: 500ms;
  animation-name: print;
  animation-fill-mode: forwards;
}
.ticket-system .receipts .receipt {
  padding: 25px 30px;
  text-align: left;
  min-height: 200px;
  width: 88%;
  background-color: #fff;
  border-radius: 10px 10px 20px 20px;
  box-shadow: 1px 3px 8px 3px rgba(0, 0, 0, 0.5);
}

.ticket-system .receipts .receipt .details {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}
.ticket-system .receipts .receipt .details .item {
  display: flex;
  flex-direction: column;
  min-width: 50%;
  padding-left: 10px;
}
.ticket-system .receipts .receipt .details .item h6 {
  margin-top: 15px;
}
.ticket-system .receipts .receipt .details .item span {
  font-size: 0.8rem;
  color: rgba(28, 28, 28, 0.801);
  font-weight: 500;
}
.ticket-system .receipts .receipt.bottom {
  /* height: 110px; */
  min-height: unset;
  position: relative;
  border-radius: 20px 20px 10px 10px;
  display: flex;
  align-items: flex-start;
  font-size: 2vw;
}
.ticket-system .receipts .receipt.bottom::before {
  content: "";
  background: linear-gradient(to right, #fff 50%, #3f32e5 50%);
  background-size: 22px 4px, 100% 4px;
  height: 4px;
  width: 90%;
  display: block;
  left: 0;
  right: 0;
  top: -1px;
  position: absolute;
  margin: auto;
}
.ticket-system .receipts .receipt.bottom {
  font-size: 1rem;
}

@keyframes print {
  0% {
    transform: translateY(-510px);
  }
  35% {
    transform: translateY(-395px);
  }
  70% {
    transform: translateY(-140px);
  }
  100% {
    transform: translateY(0);
  }
}
</style>
