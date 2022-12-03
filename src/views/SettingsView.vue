<template>
    <div class="settings" v-if="config.data.homePage">
        <div class="settingsWrapper">
          <BigTitle bigText="Domovské stránky" smallText="Nastavení" side="false"/>
          <form @change="autoUpdateConfig()" class="settingsColumn settingsCard">
            <h2>Uvítací sekce</h2>
            <div class="settingsRow">
              <label class="labelBlack">Nadpis</label>
              <input type="text" v-model="config.data.homePage.landingSection.title" />
            </div>  
            <div class="settingsRow">
              <label class="labelBlack">Podnadpis</label>
              <input type="text" v-model="config.data.homePage.landingSection.subtitle" />
            </div>    
            <h3>Pozadí</h3>
            <div class="settingsRow settingsNoLine">
              <img v-if="config.data.homePage.landingSection.background" class="imagePreview" :src="config.data.homePage.landingSection.background" />
              <img v-else class="imagePreview" :src="require('@/assets/images/noImage.jpg')" />
              <div class="settingsButtonsRow">
                <label class="settingsButton" for="settingsBackgroundUpload">
                  Nahrát
                  <img class="settingsButtonIcon" :src="require('@/assets/icons/upload.svg')" /> 
                  <input style="display: none" type="file" @input="backgroundImageInput" name="settingsBackgroundUpload" id="settingsBackgroundUpload" />
                </label>
                <div @click="deleteBackgroundImage()" class="settingsButton">
                  <label>Smazat</label>
                  <img class="settingsButtonIcon" :src="require('@/assets/icons/delete.svg')" />
                </div>
              </div>
            </div>
          </form>
          <form @change="autoUpdateConfig()" class="settingsColumn settingsCard">
            <h2>Sekce galerie</h2>
            <div class="settingsRow">
              <label class="labelBlack">Zobrazovat sekci galerie</label>
              <ToggleButton @change="autoUpdateConfig()" :isChecked="config.data.homePage.gallerySection.visible" v-model:checked="config.data.homePage.gallerySection.visible" />
            </div>  
            <div class="settingsColumn" v-if="config.data.homePage.gallerySection.visible">
              <div class="settingsRow">
                <label class="labelBlack">Nadpis</label>
                <input type="text" v-model="config.data.homePage.gallerySection.title" />
              </div>  
              <div class="settingsRow">
                <label class="labelBlack">Podnadpis</label>
                <input type="text" v-model="config.data.homePage.gallerySection.subtitle" />
              </div> 
              <div class="settingsRow">
                <label class="labelBlack">Text</label>
                <textarea v-model="config.data.homePage.gallerySection.text" />
              </div>      
              <h3>Fotografie</h3>
              <div class="settingsRow">
                <label class="labelBlack">Zobrazovat fotografie</label>
                <ToggleButton @change="autoUpdateConfig()" :isChecked="config.data.homePage.gallerySection.images.visible" v-model:checked="config.data.homePage.gallerySection.images.visible" />
              </div>  
              <div class="settingsColumn" v-if="config.data.homePage.gallerySection.images.visible" >
                <div class="settingsRow settingsNoLine" v-for="(image, index) of config.data.homePage.gallerySection.images.images" :key="image">
                  <img v-if="image" class="imagePreview" :src="image" />
                  <img v-else class="imagePreview" :src="require('@/assets/images/noImage.jpg')" />
                  <div class="settingsButtonsRow">
                    <label class="settingsButton" :for="'settingsHomepageImageUpload' + index">
                      Nahrát
                      <img class="settingsButtonIcon" :src="require('@/assets/icons/upload.svg')" />
                      <input style="display: none" type="file" @input="homePageGalleryImageInput($event, index)" :index="index" :name="'settingsHomepageImageUpload' + index" :id="'settingsHomepageImageUpload' + index" />
                    </label>
                    <div @click="deleteHomeGalleryImage(index)" class="settingsButton">
                      <label>Smazat</label>
                      <img class="settingsButtonIcon" :src="require('@/assets/icons/delete.svg')" />
                    </div>
                  </div>
                </div> 
              </div>
            </div>
          </form>
          <form @change="autoUpdateConfig()" class="settingsCard">
            <h2>Kontaktní sekce</h2>
            <div class="settingsRow">
              <label class="labelBlack">Zobrazovat kontaktní sekci</label>
              <ToggleButton @change="autoUpdateConfig()" :isChecked="config.data.homePage.contactSection.visible" v-model:checked="config.data.homePage.contactSection.visible" />
            </div>
            <div v-if="config.data.homePage.contactSection.visible" class="settingsColumn">  
              <div class="settingsRow">
                  <label class="labelBlack">Nadpis</label>
                  <input type="text" v-model="config.data.homePage.contactSection.title" />
                </div>  
                <div class="settingsRow">
                  <label class="labelBlack">Podnadpis</label>
                  <input type="text" v-model="config.data.homePage.contactSection.subtitle" />
                </div> 
                <div class="settingsRow">
                  <label class="labelBlack">Adresa</label>
                  <input type="text" v-model="config.data.homePage.contactSection.address" />
                </div>  
                <div class="settingsRow">
                  <label class="labelBlack">IČO</label>
                  <input type="text" v-model="config.data.homePage.contactSection.ico" />
                </div> 
                <div class="settingsRow">
                  <label class="labelBlack">DIČ</label>
                  <input type="text" v-model="config.data.homePage.contactSection.dic" />
                </div> 
                <div class="settingsRow">
                  <label class="labelBlack">Email</label>
                  <input type="text" v-model="config.data.homePage.contactSection.email" />
                </div> 
                <div class="settingsRow">
                  <label class="labelBlack">Telefonní číslo</label>
                  <input type="text" v-model="config.data.homePage.contactSection.phone" />
                </div> 
                <div class="settingsRow">
                  <label class="labelBlack">Zobrazovat kontaktní formulář</label>
                  <ToggleButton @change="autoUpdateConfig()" :isChecked="config.data.homePage.contactSection.contactForm.visible" v-model:checked="config.data.homePage.contactSection.contactForm.visible" />
                </div>
                <div v-if="config.data.homePage.contactSection.contactForm.visible" class="settingsColumn">
                  <div class="settingsRow">
                    <label class="labelBlack">Odesílající email</label>
                    <input type="text" />
                  </div> 
                </div>
              </div>
            </form>
            <BigTitle bigText="Stránky galerie" smallText="Nastavení" side="false"/>
            <form @change="autoUpdateConfig(); autoUpdateImages()" class="settingsColumn settingsCard">
              <div class="settingsRow">
                <label class="labelBlack">Nadpis</label>
                <input type="text" v-model="config.data.galleryPage.title" />
              </div>  
              <div class="settingsRow">
                <label class="labelBlack">Podnadpis</label>
                <input type="text" v-model="config.data.galleryPage.subtitle" />
              </div>    
              <h3>Fotografie</h3>
              <FileUpload @uploadFiles="uploadImages" >Nahrajte nové fotografie přetáhnutím</FileUpload>
              <template v-for="(image, key) of images.data" :key="key">
                <div v-if="!key.startsWith('deleted')" class="settingsRow settingsNoLine" style="margin-top: 15px">
                  <div class="settingsRow" style="justify-content: flex-start">
                    <img class="imagePreview" :src="image.link" style="margin-right: 15px" />
                    <div class="settingsColumn" style="width: fit-content; align-items: flex-start">
                      <label>Popisek</label>
                      <input v-model="image.description" />
                    </div>
                  </div>
                  <div class="settingsButtonsRow">
                    <div @click="deleteImage(key)" class="settingsButton">
                      <label>Smazat</label>
                      <img class="settingsButtonIcon" :src="require('@/assets/icons/delete.svg')" />
                    </div>
                  </div>
                </div>
              </template>
          </form>
          <BigTitle bigText="Systémové stránky" smallText="Nastavení" side="false"/>
          <form @change="autoUpdateDebts(); autoUpdateConfig()"  class="settingsColumn settingsCard">
            <h2>Finanční sekce</h2>
            <div class="settingsRow">
              <label class="labelBlack">Zobrazovat finační shrnutí</label>
              <ToggleButton @change="autoUpdateConfig()" :isChecked="config.data.dashboardPage.financeSection.visible" v-model:checked="config.data.dashboardPage.financeSection.visible" />
            </div> 
            <div v-if="config.data.dashboardPage.financeSection.visible" class="settingsColumn">
              <div class="settingsRow settingsNoLine">
                <label class="labelBlack">Číslo účtu</label>
                <input type="text" v-model="config.data.dashboardPage.financeSection.accountNumber" />
              </div> 
              <div class="settingsRow">
                <label class="labelBlack">Zůstatek na účtu</label>
                <input type="text" v-model="config.data.dashboardPage.financeSection.balance" />
              </div> 
              <div class="settingsRow">
                <label class="labelBlack">Zobrazovat půjčky</label>
                <ToggleButton @change="autoUpdateConfig()" :isChecked="config.data.dashboardPage.financeSection.debts.visible" v-model:checked="config.data.dashboardPage.financeSection.debts.visible" />
              </div> 
              <div v-if="config.data.dashboardPage.financeSection.debts.visible" class="settingsColumn">
                <h3>Půjčky</h3>
                <template v-for="(debt, key) of debts.data" :key="key">
                  <div v-if="!key.startsWith('deleted')" class="settingsRow settingsNoLine">
                    <div class="settingsColumn" style="align-items: flex-start">
                      <label>Čerpaná částka</label>
                      <input class="settingsInput" type="text" v-model="debt.total" />
                    </div>
                    <div class="settingsColumn" style="align-items: flex-start">
                      <label>Zbývající částka</label>
                      <input class="settingsInput" type="text" v-model="debt.remaining" />
                    </div>
                    <div class="settingsColumn" style="align-items: flex-start">
                      <label>Částka na byt</label>
                      <input class="settingsInput" type="text" v-model="debt.remainingPerFlat" />
                    </div>
                    <div class="settingsColumn" style="align-items: flex-start">
                      <label>Splátka na byt</label>
                      <input class="settingsInput" type="text" v-model="debt.repaymentPerFlat" />
                    </div>
                    <div @click="deleteDebt(key)" class="settingsButton">
                      <label>Smazat</label>
                      <img class="settingsButtonIcon" :src="require('@/assets/icons/delete.svg')" />
                    </div>
                  </div>
                </template>
                <div class="settingsRow settingsNoLine" style="justify-content: center">
                  <ButtonAction style="margin-right: 15px" @click="addDebt">Přidat novou půjčku</ButtonAction>
                </div>
              </div>
            </div>
          </form>
          <form @change="autoUpdateUsers()" class="settingsColumn settingsCard">
            <h2>Sekce uživatelských účtů</h2>
            <template v-for="(user, key) of users.data" :key="key">
              <div v-if="!key.startsWith('deleted')" class="settingsRow settingsNoLine">
                <div class="settingsColumn settingsItemColumn">
                  <label>Uživatelské jméno</label>
                  <input class="settingsInput" type="text" v-model="user.username" />
                </div>
                <div class="settingsColumn settingsItemColumn">
                  <label>Heslo</label>
                  <input class="settingsInput" type="password" v-model="user.password" />
                </div>
                <div class="settingsColumn" style="width: fit-content">
                  <label>Admin</label>
                  <ToggleButton @change="autoUpdateUsers()" :isChecked="user.admin" v-model:checked="user.admin" />
                </div>
                <div class="settingsColumn" style="width: fit-content">
                  <label>Aktivní</label>
                  <ToggleButton @change="autoUpdateUsers()" :isChecked="user.active" v-model:checked="user.active" />
                </div>
                <div class="settingsColumn settingsItemColumn">
                  <label>Email</label>
                  <input class="settingsInput" type="email" v-model="user.email" />
                </div>
                <div class="settingsButton" @click="deleteUser(key)" >
                  <label>Smazat</label>
                  <img class="settingsButtonIcon" :src="require('@/assets/icons/delete.svg')" />
                </div>
              </div>
            </template>
            <div class="settingsRow settingsNoLine" style="justify-content: center">
              <ButtonAction style="margin-right: 15px" @click="addUser">Přidat nového uživatele</ButtonAction>
            </div>
          </form>
        </div>
    </div>
</template>

<script>
import BigTitle from '@/components/BigTitle.vue';
import FileUpload from '@/components/FileUpload.vue';
import ToggleButton from '@/components/ToggleButton.vue';
import ButtonAction from '@/components/ButtonAction.vue';
import axios from 'axios';


export default {
  name: 'SettingsView',
  components: {
    BigTitle,
    ToggleButton,
    FileUpload,
    ButtonAction
  },
  props: {
    verified: {
      type: Boolean
    },
    permissions: {
      type: Boolean
    }
  },
  data: function(){
    return {
      config: {timeout: null, data: {}},
      images: {timeout: null, data: {}},
      debts: {timeout: null, data: {}},
      users: {timeout: null, data: {}}
    }
  },

  methods: {
    newKey: function(inputArray){
      let biggestKey = 0;

      for (let key of Object.keys(inputArray)){
        let number = key.replace(/[^0-9]/g,'');
        if (number >= biggestKey){
          biggestKey = parseInt(number);
        }
      }

      biggestKey++;
      return "new" + biggestKey;
    },

    deleteFromArray: function(key, inputArray){
      if (key.startsWith('new')){
        delete inputArray[key];
      }
      else {
        inputArray['deleted' + key] = inputArray[key];
        delete inputArray[key];
      }

      return inputArray
    },

    getConfig: function() {
      axios.get("/getConfig")
        .then((response) => {
          this.config.data = response.data;
        })
    },

    addDebt: function() {
      this.debts.data[this.newKey(this.debts.data)] = {
        "total": 0,
        "remaining": 0,
        "remainingPerFlat": 0,
        "repaymentPerFlat": 0
      }
    },

    deleteDebt: function(key) {
      this.deleteFromArray(key, this.debts.data);
      this.autoUpdateDebts();
    },

    addUser: function() {
      this.users.data[this.newKey(this.users.data)] = {
        "password": "",
        "admin": false, 
        "email": "",
        "active": false,
        "username": "Nový uživatel"
      }
    },

    deleteUser: function(key) {
      this.deleteFromArray(key, this.users.data);
      this.autoUpdateUsers();
    },

    deleteImage: function(key) {
      this.deleteFromArray(key, this.images.data);
      this.autoUpdateImages();
    },

    deleteBackgroundImage: function() {
      if (this.config.data.homePage.landingSection.background != ""){
          this.deleteImageByLink(this.config.data.homePage.landingSection.background, () => {
          this.config.data.homePage.landingSection.background = '';
          this.autoUpdateConfig();
        })
      }
      else {
        this.$notify({
            type: "warn",
            title: "Chyba v nastavení",
            text: "Toto pozadí nelze smazat"
          })
      }
    },

    deleteHomeGalleryImage: function(index) {
      if (this.config.data.homePage.gallerySection.images.images[index] != ""){
        this.deleteImageByLink(this.config.data.homePage.gallerySection.images.images[index], () => {
          this.config.data.homePage.gallerySection.images.images[index]= '';
          this.autoUpdateConfig();
        })
      }
      else {
        this.$notify({
            type: "warn",
            title: "Chyba v nastavení",
            text: "Tuto fotografii nelze smazat"
          })
      }
    },

    getDebts: function() {
      axios.get("/getAllDebts")
        .then((response) => {
          this.debts.data = response.data
        })
    },

    getUsers: function() {
      axios.get("/getAllUsers")
        .then((response) => {
          this.users.data = response.data
        })
    },

    getImages: function() {
      axios.get("/getAllImages")
        .then((response) => {
          this.images.data = response.data
        })
    },

    updateDebts: function() {
      axios.patch("/updateDebts", this.debts.data)
        .then((response) => {
          this.debts.data = response.data
        })
    },

    updateUsers: function(){
      axios.patch("/updateUsers", this.users.data)
        .then((response) => {
          this.users.data = response.data
        })
    },

    updateImages: function(){
      axios.patch("/updateImages", this.images.data)
        .then((response) => {
          setTimeout(
            this.images.data = response.data,
            200
          )
        })
    },

    uploadImage: function(image, apiPoint, callback){
      axios.put(apiPoint, image, {
          headers: {
            'Content-Type': image.type
          }
        })
          .then((response) => {
            callback(response)
          })
    },

    uploadImages: function(images){
      for (let image of images){
        this.uploadImage(image, "/uploadImage");
      }

      this.getImages();
    },

    getFileFromObject: async function(object){
      object.url = URL.createObjectURL(object);
      return new File([await fetch(object.url).then(r => r.blob())], object.name,
                      {
                        type: object.type, 
                        lastModified: new Date().getTime()
                      })
    },

    backgroundImageInput: async function(e){
      this.uploadImage(await this.getFileFromObject(e.target.files[0]),
                      "/uploadBackgroundImage",
                      (response) => {
                        this.config.data.homePage.landingSection.background = response.data
                        this.autoUpdateConfig()
                      });
    },

    homePageGalleryImageInput: async function(e, index){
      this.uploadImage(await this.getFileFromObject(e.target.files[0]),
                      "/uploadHomepageGalleryImage",
                      (response) => {
                        this.config.data.homePage.gallerySection.images.images[index] = response.data
                        this.autoUpdateConfig();
                      })
    },

    deleteImageByLink: function(link, callback){
      axios.patch("/deleteImageByLink", {"link": link})
      callback()
    },

    updateConfig: function(){
      axios.patch("/updateConfig", this.config.data)
      .then(() => {
      })
    },

    autoUpdateConfig: function(){
      if (this.config.timeout){
        clearTimeout(this.config.timeout);
      }

      this.config.timeout = setTimeout(this.updateConfig(), 250);
    },

    autoUpdateImages: function(){
      if (this.images.timeout){
        clearTimeout(this.images.timeout);
      }

      this.images.timeout = setTimeout(this.updateImages(), 500);
    },

    autoUpdateDebts: function(){
      if (this.debts.timeout){
        clearTimeout(this.debts.timeout);
        this.debts.timeout = null;
      }

      this.debts.timeout = setTimeout(this.updateDebts(), 250);
    },

    autoUpdateUsers: function(){
      if (this.users.timeout){
        clearTimeout(this.users.timeout);
      }

      this.users.timeout = setTimeout(this.updateUsers(), 250);
    }
  },

  created: function() {
    if (!this.$props.verified || !this.$props.permissions){
      this.$router.push("/login")
    }

    this.getConfig();
    this.getDebts();
    this.getUsers();
    this.getImages();
  },

  mounted: function() {

  },
  watch: {
    
  }
}
</script>

<style scoped lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap');
@import "@/assets/colors.scss";

.settings {
  padding: 90px 0 0 0;
  min-height: 74vh;
  margin: 0;
  overflow-x: hidden;
}

.settingsWrapper {
  display: flex;
  flex-flow: column nowrap;
  width: 100%;
  justify-content: flex-start;
  align-items: center;
}

.settingsRow {
  width: 100%;
  display: flex;
  flex-flow: row nowrap;
  align-items: center;
  justify-content: space-between; 
  margin-bottom: 15px;
  border-bottom: $shadows-light solid 1px;
}

.settingsNoLine {
  border-bottom: none;
}

.settingsColumn {
  width: 100%;
  display: flex;
  flex-flow: column nowrap;
  align-items: center;
  justify-content: flex-start;
}

.settingsItemColumn {
  align-items: flex-start;
  margin: 0;
  width: fit-content;
}

.settingsCard {
  width: 70%;
  padding: 3% 5%;
  box-shadow: 10px 10px 40px #D8D8D8;
  margin: 3%;
  transition: all 220ms ease-in-out;
  box-sizing: border-box;
}

.imagePreview {
  width: 100px;
  height: 100px;
  object-fit: cover;
}

.imageBackground {
  width: 70%;
  object-fit: cover;
  max-height: 500px;
}

.settingsButtonsRow {
  display: flex;
  flex-flow: row nowrap;
  align-items: center;
  justify-content: flex-start;
}

.settingsButton {
  display: flex;
  flex-flow: column nowrap;
  align-items: center;
  justify-content: flex-start;
  margin-left: 15px;
  transition: all 120ms ease-in-out;
  cursor: pointer;

  &:hover {
    filter: brightness(1.2);
  }

  .settingsButtonIcon {
    height: 3rem;
    width: 3rem;
  }
}

.settingsInput {
  max-width: 10vw;
}

.slide-top-enter-active, .slide-top-leave-active {
  transition: all 220ms ease-in-out;
}

.slide-top-enter-from, .slide-top-leave-to {
  transform: translateY(50px);
  opacity: 0;
  max-height: 0px;
}

.slide-top-enter-to, .slide-top-leave-from {
  transform: translateY(0px);
  opacity: 1;
  max-height: 50px;
}

.slide-top-move {
  transition: all 220ms ease-in-out;
}

@media (max-width: 600px) {
  .settingsCard {
    width: 100%;
  }
}

</style>
