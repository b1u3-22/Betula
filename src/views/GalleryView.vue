<template>
  <div class="gallery">
    <div class="galleryBigContainer">
      
      <BigTitle style="margin: 0 0 25px 0" side="false" :smallText="generalInfo.main_gallery_subtitle" :bigText="generalInfo.main_gallery_title" />

      <div class="galleryMainContainer">
        <div class="galleryColumn">
          <template v-for="image in column_0" :key="image.pictureID">
            <div class="galleryImageItem">
              <img class="galleryImage" :src="image.link" />
              <div v-if="image.description != '' && image.description != 'Titulek fotky'" class="galleryImageOverlay">{{ image.description }}</div>
            </div>
          </template>
        </div>
        <div class="galleryColumn">
          <template v-for="image in column_1" :key="image.pictureID">
            <div class="galleryImageItem">
              <img class="galleryImage" :src="image.link" />
              <div v-if="image.description != '' && image.description != 'Titulek fotky'" class="galleryImageOverlay">{{ image.description }}</div>
            </div>
          </template>
        </div>
        <div class="galleryColumn">
          <template v-for="image in column_2" :key="image.pictureID">
            <div class="galleryImageItem">
              <img class="galleryImage" :src="image.link" />
              <div v-if="image.description != '' && image.description != 'Titulek fotky'" class="galleryImageOverlay">{{ image.description }}</div>
            </div>
          </template>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import BigTitle from '@/components/BigTitle.vue';
import axios from 'axios';
// @ is an alias to /src


export default {
  name: 'GalleryView',
  components: {
    BigTitle
  },
  data: function() {
    return {
      column_0: [],
      column_1: [],
      column_2: [],
      generalInfo: {},
      pictures: []
    }
  },

  created: function() {
    axios
      .get("http://127.0.0.1:5000/getGeneralInfo")
      .then((response) => {
        for (const [key, value] of Object.entries(response.data)){
          this.generalInfo[key] = value.text
        }
      });

      
  },

  mounted: function() {
    window.scrollTo({top: 0, behavior: 'auto'});

    axios
    .get("http://127.0.0.1:5000/getAllPictures")
    .then((response) => {
        for (const [key, value] of Object.entries(response.data)){
            this.pictures.push({
                pictureID: key,
                link: value.link,
                description: value.description,
            })
        }  
        let imgs_per_clmn = Math.floor(this.pictures.length / 3);
        console.log(this.pictures.length)

        for (let i = 0; i < imgs_per_clmn; i++) {
          this.column_0.push(this.pictures[i]);
        }

        for (let i = this.column_0.length; i < imgs_per_clmn + this.column_0.length; i++) {
          this.column_1.push(this.pictures[i]);
        } 

        for (let i = this.column_1.length + this.column_0.length; i < this.pictures.length; i++){
          this.column_2.push(this.pictures[i]);
        }
    });
  }
}
</script>

<style scoped lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap');
@import "@/assets/colors.scss";

.gallery {
  padding: 90px 0 0 0;
  min-height: 74vh;
  margin: 0;
  overflow-x: hidden;

  .galleryBigContainer {
    display: flex;
    flex-flow: column nowrap;
    justify-content: flex-start;
    align-items: center;

    .galleryMainContainer {
      display: flex;
      flex-flow: row nowrap;
      justify-content: space-evenly;
      align-items: flex-start;

      .galleryColumn {
        display: flex;
        flex-flow: column nowrap;
        justify-content: flex-start;
        align-items: center;

        .galleryImageItem {
          position: relative;
          //cursor: pointer;
          margin: 10px;
          //box-shadow: 10px 10px 40px #D8D8D8;

          .galleryImage {
            width: 100%;
            height: 100%;
            object-fit: cover;
          }

          .galleryImageOverlay {
            position: absolute;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            display: flex;
            flex-flow: column nowrap;
            align-items: center;
            justify-content: center;
            opacity: 0;
            color: $background-light;
            transition: all ease-in-out 220ms;
            cursor: pointer;

            &:hover {
              opacity: 0.85;
              background-color: $text-light;
            } //   TODO: FOR FUTURE USE
          }
        }

      }
    }
  }
}

@media (max-width: 600px) {
  .galleryMainContainer {
    flex-flow: column nowrap !important; 
  }
}


</style>