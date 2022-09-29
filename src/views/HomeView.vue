<template>
  <div class="home">
    <img :src="require(`@/assets/images/photo62.jpeg`)" class="landingPageImage" />
    <div id="home" class="landingPageContainer">
      <h1 class="homeTitle">Bytové družstvo</h1>
      <h2 class="homeSubtitle">Břízová 186 - 189, Lutín</h2>
    </div>
    <div id="home-gallery" class="homeGalleryContainer">
      <div class="homeGalleryLeftContainer">
        <BigTitle side="true" smallText="Galerie" bigText="Něco o nás"/>
        <p class="homeGalleryText">Sed egestas, lorem ac dictum sagittis, sem mauris ultrices neque, eget ornare justo ex ac lacus. 

Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.</p>
        <ButtonLink style="margin: 0 0 0 56px;" link="gallery">Celá galerie</ButtonLink>
      </div>
      <div class="homeGalleryRightContainer">
          <figure>
            <img :src="require(`@/assets/images/photo61.jpeg`)"/>
            <img :src="require(`@/assets/images/photo1.jpeg`)"/>
            <img :src="require(`@/assets/images/photo62.jpeg`)"/>
          </figure>
      </div>
    </div>
    <div id="home-contact" class="homeContactContainer">
      <BigTitle side="false" smallText="kontakt" bigText="Napište nám" />
      <div class="homeContactContentContainer">
        <div class="homeContactLeftContainer">
          <h3 class="homeContactSubtitle">Kontaktní informace</h3>
          <div class="homeContactItemContainer">
            <img class="homeContactItemIcon" :src="require(`@/assets/icons/house.svg`)" />
            <div class="homeContactItemText">Břízová 186 - 189, Lutín, 783 49</div>
          </div>
          <div class="homeContactItemContainer">
            <img class="homeContactItemIcon" :src="require(`@/assets/icons/phone.svg`)" />
            <div class="homeContactItemText">+420 156 564 456</div>
          </div>
          <div class="homeContactItemContainer">
            <img class="homeContactItemIcon" :src="require(`@/assets/icons/phone.svg`)" />
            <div class="homeContactItemText">+420 156 564 456</div>
          </div>
          <div class="homeContactItemContainer">
            <img class="homeContactItemIcon" :src="require(`@/assets/icons/mail.svg`)" />
            <div class="homeContactItemText">info@betula.cz</div>
          </div>
        </div>
        <form class="homeContactForm">
          <h3 class="homeContactSubtitle">Kontaktní formulář</h3>
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

export default {
  name: 'HomeView',
  components: {
    BigTitle,
    ButtonLink
  },
  mounted: function() {
    let path = this.$route.path.replace('/', '');
    path === '' ? path = 'home' : '';
    if (path.includes('home')){
        document.getElementById(path).scrollIntoView({behavior: "smooth"})
    }
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
  margin: 7% 0 0 0;
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
    color: $background-dark;
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
          color: $background-dark
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
        border-bottom: solid 2px $background-dark;
        background-color: $background-light;
        width: 100%;
        color: $background-dark;
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