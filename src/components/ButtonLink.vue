<template>
    <div @click="goTo">
      <button class="buttonLinkContainer">
        <slot></slot>
      </button>
    </div>  
    
</template>

<script>
export default {
  name: 'ButtonLink',
  components: {

  },
  props: {
    link: {
      type: String
    },
    target: {
      type: String,
      default: "_self"
    }
  },

  methods: {
    goTo: function() {
      this.$router.push(this.link)
    }
  },

  data: function () {
      return {
          
      }
  }
}
</script>

<style scoped lang="scss">

@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap');
@import "@/assets/colors.scss";

.buttonLinkContainer {
    background-position: center;
    transition: background 400ms;
    border: none;
    padding: 8px 14px;
    background-color: $primary;
    box-shadow: 0px 3px 3px rgba(0, 0, 0, 0.25);
    cursor: pointer;
    text-decoration: none;
    font-size: 0.875;
    font-weight: 700;
    color: $background-light;
    font-family: 'Montserrat', sans-serif;


    &:hover {
      background: $primary radial-gradient(circle, transparent 1%, $primary 1%) center/15000%;
    }

    &:active {
      background-color: $secondary;
      background-size: 100%;
      transition: background 0ms;
    }
}

</style>
