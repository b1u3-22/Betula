<template>
    <div class="bigTitleContainer" :class="{bigTitleContainerSide: side === 'true', bigTitleContainerNormal: side === 'false'}" >
        <div class="bigTitleLine" />
        <div class="bigTitleTextContainer">
            <div class="bigTitleSmallText" :style="smallTextStyle">{{ smallText }}</div>
            <div class="bigTitleBigText" :style="bigTextStyle">{{ bigText }}</div>
        </div>
    </div>

</template>

<script>
export default {
  name: 'BigTitle',
  components: {

  },
  props: [
      'side', 'smallText', 'bigText', 'smallTextStyle', 'bigTextStyle'
  ],

  methods: {
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

.bigTitleContainer {
    display: flex;
    width: fit-content;
}

.bigTitleContainerSide {
    flex-flow: row nowrap;
    justify-content: flex-start;
    align-items: stretch;
    width: 100%;

    .bigTitleLine {
        background-color: $primary;
        width: 6px;
        margin: 0 25px;
    }

    .bigTitleTextContainer {
        display: flex;
        flex-flow: column nowrap;
        justify-content: flex-start;
        align-items: flex-start;

        .bigTitleBigText {
            text-align: left;
        } 
    }
}

.bigTitleContainerNormal {
    flex-flow: column-reverse nowrap;
    justify-content: center;
    align-items: center;

    .bigTitleLine {
        background-color: $primary;
        width: 25%;
        height: 6px;
        margin: 10px 0;
    }

    .bigTitleTextContainer {
        display: flex;
        flex-flow: column nowrap;
        justify-content: center;
        align-items: center;
    
        .bigTitleBigText {
            text-align: center;
        } 
    }
}

.bigTitleSmallText {
    color: $primary;
    font-size: 1.125rem;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    font-weight: 700;
    margin: 0 0 0 0.25em;
}

.bigTitleBigText {
    color: $background-dark;
    font-size: 4.375rem;
    font-weight: 700;
}

@media (max-width: 600px) {
    .bigTitleContainerSide {
        flex-flow: column-reverse nowrap;
        justify-content: center;
        align-items: center;

        .bigTitleLine {
            background-color: $primary;
            width: 25%;
            height: 6px;
            margin: 10px 0;
        }

        .bigTitleTextContainer {
            display: flex;
            flex-flow: column nowrap;
            justify-content: center;
            align-items: center;
        
            .bigTitleBigText {
                text-align: center;
            } 
        }
    }
}

</style>
