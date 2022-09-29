<template>
    <div class="contentCard">
        <BigTitle side="true" :bigText="title" :smallText="timestamp" smallTextStyle="font-size: 1rem" bigTextStyle="font-size: 3.5rem" />
        <p class="contentCardMainText">
            <slot />
        </p>
    </div>
</template>

<script>
import BigTitle from './BigTitle.vue';


export default {
  name: 'ContentCard',
  components: {
    BigTitle
},
  props: [
    "title", "timestamp"
  ],

  methods: {

  },

  data: function () {
      return {
      }
  },
}

</script>

<style scoped lang="scss">

@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap');
@import "@/assets/colors.scss";

.contentCard {
    display: flex;
    flex-flow: column nowrap;
    align-items: flex-start;
    justify-content: stretch;
    width: 80%;
    box-shadow: 10px 10px 40px #D8D8D8;
    padding: 3% 5%;
    margin: 5% 0;

    .contentCardMainText {
        font-weight: 400;
        font-size: 1.2rem;
        text-align: left;
        margin: 5% 0 0 50px;
    }
}

</style>
