<template>
  <div class="home" v-if="config.landingSection">
    <img v-if="config.landingSection.background" :src="config.landingSection.background" class="landingPageImage" />
    <img v-else :src="require('@/assets/images/noImageNoLogo.jpg')" class="landingPageImage" />
    <div id="home" class="landingPageContainer">
      <h1 class="homeTitle">{{ config.landingSection.title }}</h1>
      <h2 class="homeSubtitle">{{ config.landingSection.subtitle }}</h2>
    </div>
    <div v-if="config.gallerySection.visible" id="home-gallery" class="homeGalleryContainer"
     :style="config.gallerySection.images.visible ? 'justify-content: flex-end;' : 'justify-content: center;'">
      <div class="homeGalleryLeftContainer" :style="config.gallerySection.images.visible ? 'margin: 0 10em 0 0; align-items: flex-start;' : 'margin: 0; align-items: center;'" >
        <BigTitle :side="config.gallerySection.images.visible ? 'true' : 'false'" :smallText="config.gallerySection.subtitle" :bigText="config.gallerySection.title"/>
        <p class="homeGalleryText" :style="config.gallerySection.images.visible ? 'margin: 25px 0 20px 60px;' : 'margin: 25px 0 20px 0;'">{{ config.gallerySection.text }}</p>
        <ButtonLink :style="config.gallerySection.images.visible ?  'margin: 0 0 0 56px;' : 'margin: 0;'" link="gallery">Celá galerie</ButtonLink>
      </div>
      <div v-if="config.gallerySection.images.visible" class="homeGalleryRightContainer">
          <figure>
            <img v-if="config.gallerySection.images.images[0]" :src="config.gallerySection.images.images[0]"/>
            <img v-else :src="require('@/assets/images/noImageNoLogo.jpg')"/>
            <img v-if="config.gallerySection.images.images[1]" :src="config.gallerySection.images.images[0]"/>
            <img v-else :src="require('@/assets/images/noImage.jpg')"/>
            <img v-if="config.gallerySection.images.images[2]" :src="config.gallerySection.images.images[0]"/>
            <img v-else :src="require('@/assets/images/noImageNoLogo.jpg')"/>
          </figure>
      </div>
    </div>
    <div v-if="config.contactSection.visible" id="home-contact" class="homeContactContainer">
      <BigTitle side="false" :smallText="config.contactSection.subtitle" :bigText="config.contactSection.title" />
      <div class="homeContactContentContainer">
        <div class="homeContactLeftContainer" :style="config.contactSection.contactForm.visible ? 'width: 30%' : 'widtch: fit-content'">
          <h3 class="homeContactSubtitle">Kontaktní informace</h3>
          <div class="homeContactItemContainer">
            <img class="homeContactItemIcon" :src="require(`@/assets/icons/house.svg`)" />
            <div class="homeContactItemText">{{ config.contactSection.address }}</div>
          </div>
          <div class="homeContactItemContainer">
            <img class="homeContactItemIcon" :src="require(`@/assets/icons/phone.svg`)" />
            <div class="homeContactItemText">{{ config.contactSection.phone }}</div>
          </div>
          <div class="homeContactItemContainer">
            <img class="homeContactItemIcon" :src="require(`@/assets/icons/mail.svg`)" />
            <div class="homeContactItemText">{{ config.contactSection.email }}</div>
          </div>
          <div class="homeContactItemContainer">
            <img class="homeContactItemIcon" :src="require(`@/assets/icons/ico.svg`)" />
            <div class="homeContactItemText">{{ config.contactSection.ico }}</div>
          </div>
          <div class="homeContactItemContainer">
            <img class="homeContactItemIcon" :src="require(`@/assets/icons/dic.svg`)" />
            <div class="homeContactItemText">{{ config.contactSection.dic }}</div>
          </div>
        </div>
        <form v-if="config.contactSection.contactForm.visible" class="homeContactForm">
          <h3>Kontaktní formulář</h3>
          <label class="homeContactFormLabel" for="email">Váš email *</label>
          <input class="homeContactFormInput" type="email" id="email" name="email" placeholder="jannovak@seznam.cz">
          <label class="homeContactFormLabel" for="subject">Co Vás zajímá *</label>
          <input class="homeContactFormInput" type="text" id="subject" name="subject" placeholder="Úklid na chodbě 2. patro">
          <label class="homeContactFormLabel" for="message">Vaše zpráva *</label>
          <textarea class="homeContactFormInput" style="height: 15vh;" type="text" id="message" name="message" placeholder="Vaše detailnější sdělení" />
          <div class="homeContactFormBottomContainer">
            <p class="homeContactFormWarning">* Toto pole je povinné</p>
            <ButtonLink>Odeslat</ButtonLink>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import BigTitle from '@/components/BigTitle.vue';
import ButtonLink from '@/components/ButtonLink.vue';
import axios from 'axios';

export default {
  name: 'HomeView',
  components: {
    BigTitle,
    ButtonLink
  },
  data: function(){
    return {
      config: {}
    }
  },
  mounted: function() {
    let path = this.$route.path.replace('/', '');
    path === '' ? path = 'home' : '';
    if (path.includes('home')){
        //document.getElementById(path).scrollIntoView({behavior: "smooth"})
    }
  },

  created: function() {
    axios
      .get("/getHomePageConfig")
      .then((response) => {
        this.config = response.data;
      });
  },

  watch: {
    $route: function(to){
      let path = to.path.replace('/', '')
      path === '' ? path = 'home' : '';
      if (path.includes('home')){
        document.getElementById(path).scrollIntoView({behavior: "smooth"})
      }
    }
  }
}
</script>

<style scoped lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap');
@import "@/assets/colors.scss";

.home {
  margin: 0;
  padding: 0;
  overflow-x: hidden;
}

.landingPageImage {
  z-index: 1;
  display: block;
  object-fit: cover;
  width: 110%;
  height: 100vh;
  margin: 0 0 -100vh -3px;
  padding: 0;
  filter: brightness(0.35);
}

.landingPageContainer {
  width: 100%;
  height: 100vh;
  display: flex;
  flex-flow: column nowrap;
  align-items: center;
  justify-content: center;
  
  .homeTitle {
    z-index: 2;
    color: $background-light;
    font-size: 6.25rem;
    font-weight: 700;
    margin: 0;
  }

  .homeSubtitle {
    z-index: 2;
    color: $background-light;
    font-size: 3.5rem;
    font-weight: 600;
  }
}

.homeGalleryContainer {
  display: flex;
  flex-flow: row wrap;
  width: 100vw;
  height: fit-content;
  margin: 7% 0 7% 0;
  align-items:center;
  justify-content: flex-end;

  .homeGalleryLeftContainer {
    display: flex;
    flex-flow: column nowrap;
    align-items: flex-start;
    justify-content: flex-start;
    width: 30%;
    margin: 0 10em 0 0;

    .homeGalleryText {
      margin: 25px 0 20px 60px;
      text-align: left;
      font-size: 1.125rem;
      font-weight: 400;
    } 
  }

  .homeGalleryRightContainer {
    background: linear-gradient(90deg, #FFFFFF 0%, rgba(255, 255, 255, 0) 23.52%, rgba(255, 255, 255, 0) 74.48%, #FFFFFF 100%);
    z-index: 3;
    position: relative;
    overflow: visible;
    width: 50%;
    clip-path: inset( -100vw -100vw -100vw 0 );
    

    figure {
      z-index: 1;
      position: relative;
      width: 270%;
      margin: 0;
      left: 0;
      display: flex;
      flex-flow: row nowrap;
      animation: homeGalleryAnimation 15s ease-in-out infinite;
      max-height: 45vh;

      img {
        z-index: 2;
        width: 30%;
        float: left;
        margin: 0 3% 0 0;
        filter: drop-shadow(10px 10px 20px rgba(0, 0, 0, 0.5));
        object-fit: cover;
      }
    }
  }
}

.homeContactContainer {
  width: 100vw;
  display: flex;
  flex-flow: column nowrap;
  justify-content: flex-start;
  align-items: center;
  margin: 7% 0 0 0;

  .homeContactSubtitle {
    font-size: 2.2rem;
    font-weight: 700;
    color: $text-light;
  }

  .homeContactContentContainer {
    display: flex;
    flex-flow: row wrap;
    align-items: center;
    justify-content: space-evenly;
    width: 100%;
    margin: 4% 0 0 0;
    padding: 0 0 7% 0;

    .homeContactLeftContainer {
      width: 30%;

      .homeContactSubtitle {
        text-align: left;
      }

      .homeContactItemContainer {
        width: 100%;
        display: flex;
        flex-flow: row nowrap;
        justify-content: flex-start;
        align-items: center;
        margin: 0 0 22px 0;

        .homeContactItemIcon {
          margin: 0 22px 0 0;
          height: 30px;
          width: auto;
        }

        .homeContactItemText {
          font-size: 1.25rem;
          font-weight: 400;
          color: $text-light
        }
      }
    }

    .homeContactForm {
      display: flex;
      flex-flow: column nowrap;
      align-items: flex-start;
      justify-content: flex-start;
      width: 25%;
      padding: 3% 3%;
      box-shadow: 10px 10px 40px #D8D8D8;

      .homeContactFormLabel {
        font-weight: 700;
        font-size: 0.75rem;
        color: $primary;
        margin: 0 0 10px 0;
      }

      .homeContactFormInput {
        border: none;
        border-bottom: solid 2px $text-light;
        background-color: $background-light;
        width: 100%;
        color: $text-light;
        font-size: 1.125rem;
        font-weight: 500;
        margin: 0 0 22px 0;
        transition: all 220ms ease-in-out;
        font-family: 'Montserrat', sans-serif;
        resize: none;
        

        &:focus {
          outline: none;
          border-color: $primary;
        }

        &::placeholder {
          color: #A7A7A7;
          font-weight: 400;
        }
      }

      .homeContactFormBottomContainer {
        display: flex;
        flex-flow: column nowrap;
        justify-content: flex-start;
        width: 100%;
        align-items: flex-end;

        .homeContactFormWarning {
          color: $primary;
          font-weight: 400;
          font-size: 0.625rem;
        }
      }
    }
  }
}

@keyframes homeGalleryAnimation {
  0% {
    left: 0;
  }

  20% {
    left: 0;
  }

  30% {
    left: -89.5%;
  }

  50% {
    left: -89.5%;
  }

  60% {
    left: -178.5%;
  }

  80% {
    left: -178.5%;
  }

  100% {
    left: 0;
  }

}

@keyframes homeGalleryAnimationMobile {
  0% {
    left: 89.5%;
  }

  20% {
    left: 89.5%;
  }

  30% {
    left: 0;
  }

  50% {
    left: 0;
  }

  60% {
    left: -89.5%;
  }

  80% {
    left: -89.5%;
  }

  100% {
    left: 89.5%;
  }

}

@media (max-width: 600px) {
  .homeGalleryContainer {
    flex-flow: column nowrap;

    .homeGalleryLeftContainer {
      width: 100%;
      margin: 0;
      align-items: center;

      .homeGalleryText {
        margin: 25px 60px 20px 60px;
        text-align: center;
      }

      .buttonLinkContainer {
        margin: 0 !important;
      }
    }

    .homeGalleryRightContainer {
      width: 100%;
      display: flex;
      flex-flow: column nowrap;
      align-items: center;
      justify-content: center;
      margin: 5% 0 0 0;

      figure {
        animation: homeGalleryAnimationMobile 15s ease-in-out infinite;
        margin: 0 0 0 10%;
      }
    }
  }

  .homeContactContainer {
    margin: 15% 0 0 0;

    .homeContactContentContainer {
      flex-flow: column nowrap;

      .homeContactLeftContainer {
        width: 100%;

        .homeContactSubtitle {
          text-align: center;
        }

        .homeContactItemContainer {
          width: 100%;
          align-items: center;
          justify-content: center;
        }
      }

      .homeContactForm {
        width: 95%;

        .homeContactSubtitle {
          width: 100%;
        }

        .homeContactFormBottomContainer {
          justify-content: flex-start;
          align-items: center;
        }
      }
    }
  }
}


</style>