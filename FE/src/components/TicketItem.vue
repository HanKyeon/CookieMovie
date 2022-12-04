<template>
  <main id="ticket">
    <div class="ticket-wrapper">
      <div class="ticket top">
        <span>No. 187</span>
        <h2 class="text-right">Movie Title</h2>
        <img
          src="https://www.themoviedb.org/t/p/w600_and_h900_bestv2/eTOqjSNjMUpnjbRCnYElU4b5uWW.jpg"
          alt=""
          class="poster"
        />
        <div class="details">
          <div class="item">
            <h4>Date</h4>
            <span>2022-11-19</span>
          </div>
          <div class="item">
            <h4>RATE</h4>
            <rating-component />
          </div>
        </div>
      </div>
      <div class="ticket bottom">
        <div class="item">
          <h4>Review</h4>
          <span
            >이것은 짧은 리뷰입니다.이것은 짧은 리뷰입니다.이것은 짧은
            리뷰입니다.</span
          >
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import RatingComponent from "./RatingComponent.vue";
export default {
  name: "TicketItem",
  components: {
    RatingComponent,
  },
};
</script>

<style>
#ticket {
  /* max-width: 40%; */
  color: black;
}

#ticket .poster {
  max-width: 100%;
  /* flex-shrink: 1; */
}

#ticket .ticket-wrapper {
  overflow: hidden;
  padding-bottom: 10px;
  width: 100%;
  display: flex;
  align-items: center;
  flex-direction: column;
  /* flex-shrink: 1; */
}

#ticket .ticket {
  padding: 25px 30px;
  text-align: left;
  min-height: 200px;
  width: 88%;
  background-color: #fff;
  border-radius: 10px 10px 20px 20px;
  box-shadow: 1px 3px 8px 3px rgba(0, 0, 0, 0.5);
}

#ticket .ticket .details {
  flex-shrink: 1;
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}
#ticket .ticket .details .item {
  display: flex;
  flex-direction: column;
  min-width: 50%;
  padding-left: 10px;
}
#ticket .ticket .details .item h4 {
  margin-top: 15px;
}
#ticket .ticket .details .item span {
  font-size: 1em;
  color: rgba(28, 28, 28, 0.801);
  font-weight: 500;
}
#ticket .ticket.bottom {
  /* height: 110px; */
  min-height: unset;
  position: relative;
  border-radius: 20px 20px 10px 10px;
  display: flex;
  align-items: flex-start;
  font-size: 2vw;
}
#ticket .ticket.bottom::before {
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
#ticket .ticket.bottom {
  font-size: 1em;
}
</style>
