<template>
    <div class="settings">
        <div class="settingsWrapper">
          <BigTitle bigText="Domovské stránky" smallText="Nastavení" side="false"/>
          <form class="settingsColumn settingsCard">
            <h2>Uvítací sekce</h2>
            <div class="settingsRow">
              <label class="labelBlack">Nadpis</label>
              <input type="text" v-model="config.homePage.landingSection.title" />
            </div>  
            <div class="settingsRow">
              <label class="labelBlack">Podnadpis</label>
              <input type="text" v-model="config.homePage.landingSection.subtitle" />
            </div>    
            <h3>Pozadí</h3>
            <div class="settingsRow">
              <img class="imagePreview" :src="config.homePage.landingSection.background" />
              <div class="settingsButtonsRow">
                <label class="settingsButton" for="settingsBackgroundUpload">
                  Nahrát
                  <img class="settingsButtonIcon" :src="require('@/assets/icons/upload.svg')" />
                  <input style="display: none" type="file" name="settingsBackgroundUpload" id="settingsBackgroundUpload" />
                </label>
                <div class="settingsButton">
                  <label>Smazat</label>
                  <img class="settingsButtonIcon" :src="require('@/assets/icons/delete.svg')" />
                </div>
              </div>
            </div>
          </form>
          <form class="settingsColumn settingsCard">
            <h2>Sekce galerie</h2>
            <div class="settingsRow">
              <label class="labelBlack">Zobrazovat sekci galerie</label>
              <ToggleButton :isChecked="config.homePage.gallerySection.visible" v-model:checked="config.homePage.gallerySection.visible" />
            </div>  
            <div class="settingsColumn" v-if="config.homePage.gallerySection.visible">
              <div class="settingsRow">
                <label class="labelBlack">Nadpis</label>
                <input type="text" v-model="config.galleryPage.title" />
              </div>  
              <div class="settingsRow">
                <label class="labelBlack">Podnadpis</label>
                <input type="text" v-model="config.homePage.gallerySection.subtitle" />
              </div> 
              <div class="settingsRow">
                <label class="labelBlack">Text</label>
                <textarea v-model="config.homePage.gallerySection.text" />
              </div>      
              <h3>Fotografie</h3>
              <div class="settingsRow">
                <label class="labelBlack">Zobrazovat fotografie</label>
                <ToggleButton :isChecked="config.homePage.gallerySection.images.visible" v-model:checked="config.homePage.gallerySection.images.visible" />
              </div>  
              <div class="settingsColumn" v-if="config.homePage.gallerySection.images.visible" >
                <div class="settingsRow" v-for="image of config.homePage.gallerySection.images.images" :key="image">
                  <img class="imagePreview" :src="image" />
                  <div class="settingsButtonsRow">
                    <label class="settingsButton" for="settingsBackgroundUpload">
                      Nahrát
                      <img class="settingsButtonIcon" :src="require('@/assets/icons/upload.svg')" />
                      <input style="display: none" type="file" name="settingsBackgroundUpload" id="settingsBackgroundUpload" />
                    </label>
                    <div class="settingsButton">
                      <label>Smazat</label>
                      <img class="settingsButtonIcon" :src="require('@/assets/icons/delete.svg')" />
                    </div>
                  </div>
                </div> 
              </div>
            </div>
          </form>
          <form class="settingsCard">
            <h2>Kontaktní sekce</h2>
            <div class="settingsRow">
              <label class="labelBlack">Zobrazovat kontaktní sekci</label>
              <ToggleButton :isChecked="config.homePage.contactSection.visible" v-model:checked="config.homePage.contactSection.visible" />
            </div>
            <div v-if="config.homePage.contactSection.visible" class="settingsColumn">  
              <div class="settingsRow">
                  <label class="labelBlack">Nadpis</label>
                  <input type="text" v-model="config.homePage.contactSection.title" />
                </div>  
                <div class="settingsRow">
                  <label class="labelBlack">Podnadpis</label>
                  <input type="text" v-model="config.homePage.contactSection.subtitle" />
                </div> 
                <div class="settingsRow">
                  <label class="labelBlack">Adresa</label>
                  <input type="text" v-model="config.homePage.contactSection.address" />
                </div>  
                <div class="settingsRow">
                  <label class="labelBlack">IČO</label>
                  <input type="text" v-model="config.homePage.contactSection.ico" />
                </div> 
                <div class="settingsRow">
                  <label class="labelBlack">DIČ</label>
                  <input type="text" v-model="config.homePage.contactSection.dic" />
                </div> 
                <div class="settingsRow">
                  <label class="labelBlack">Email</label>
                  <input type="text" v-model="config.homePage.contactSection.email" />
                </div> 
                <div class="settingsRow">
                  <label class="labelBlack">Telefonní číslo</label>
                  <input type="text" v-model="config.homePage.contactSection.phone" />
                </div> 
                <div class="settingsRow">
                  <label class="labelBlack">Zobrazovat kontaktní formulář</label>
                  <ToggleButton :isChecked="config.homePage.contactSection.contactForm.visible" v-model:checked="config.homePage.contactSection.contactForm.visible" />
                </div>
                <div v-if="config.homePage.contactSection.contactForm.visible" class="settingsColumn">
                  <div class="settingsRow">
                    <label class="labelBlack">Odesílající email</label>
                    <input type="text" />
                  </div> 
                </div>
              </div>
            </form>
            <BigTitle bigText="Stránky galerie" smallText="Nastavení" side="false"/>
            <form class="settingsColumn settingsCard">
              <div class="settingsRow">
                <label class="labelBlack">Nadpis</label>
                <input type="text" v-model="config.galleryPage.title" />
              </div>  
              <div class="settingsRow">
                <label class="labelBlack">Podnadpis</label>
                <input type="text" v-model="config.galleryPage.subtitle" />
              </div>    
              <h3>Fotografie</h3>
              <FileUpload>Nahrajte nové fotografie přetáhnutím</FileUpload>
              <div class="settingsRow" style="margin-top: 15px">
                <div class="settingsRow" style="justify-content: flex-start">
                  <img class="imagePreview" src="https://picsum.photos/500" style="margin-right: 15px" />
                  <div class="settingsColumn" style="width: fit-content; align-items: flex-start">
                    <label>Popisek</label>
                    <input />
                  </div>
                </div>
                
                <div class="settingsButtonsRow">
                  <div class="settingsButton">
                    <label>Smazat</label>
                    <img class="settingsButtonIcon" :src="require('@/assets/icons/delete.svg')" />
                  </div>
                </div>
              </div>
          </form>
          <BigTitle bigText="Systémové stránky" smallText="Nastavení" side="false"/>
          <form class="settingsColumn settingsCard">
            <h2>Finanční sekce</h2>
            <div class="settingsRow">
              <label class="labelBlack">Zobrazovat finační shrnutí</label>
              <ToggleButton :isChecked="config.dashboardPage.financeSection.visible" v-model:checked="config.dashboardPage.financeSection.visible" />
            </div> 
            <div v-if="config.dashboardPage.financeSection.visible" class="settingsColumn">
              <div class="settingsRow">
                <label class="labelBlack">Číslo účtu</label>
                <input type="text" v-model="config.dashboardPage.financeSection.accountNumber" />
              </div> 
              <div class="settingsRow">
                <label class="labelBlack">Zůstatek na účtu</label>
                <input type="text" v-model="config.dashboardPage.financeSection.balance" />
              </div> 
              <div class="settingsRow">
                <label class="labelBlack">Zobrazovat půjčky</label>
                <ToggleButton :isChecked="config.dashboardPage.financeSection.debts.visible" v-model:checked="config.dashboardPage.financeSection.debts.visible" />
              </div> 
              <div v-if="config.dashboardPage.financeSection.debts.visible" class="settingsColumn">
                <h3>Půjčky</h3>
                <template v-for="(debt, key) of debts" :key="key">
                  <div v-if="!key.startsWith('deleted')" class="settingsRow">
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
                <div class="settingsRow" style="justify-content: center">
                  <ButtonAction style="margin-right: 15px" @click="addDebt">Přidat novou půjčku</ButtonAction>
                  <ButtonAction @click="updateDebts">Uložit půjčky</ButtonAction>
                </div>
              </div>
            </div>
          </form>
          <form class="settingsColumn settingsCard">
            <h2>Sekce uživatelských účtů</h2>
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
  data: function(){
    return {
      config: {},
      images: {},
      debts: {},
      users: {}
    }
  },

  methods: {
    getConfig: function() {
      axios.get("/getConfig")
        .then((response) => {
          console.log(response);
          this.config = response.data;
        })
    },

    addDebt: function() {
      let biggestKey = 0;

      for (let key of Object.keys(this.debts)){
        let number = key.replace(/[^0-9]/g,'');
        if (number >= biggestKey){
          biggestKey = parseInt(number);
        }
      }

      biggestKey += 1;

      this.debts["new" + biggestKey] = {
        "total": 0,
        "remaining": 0,
        "remainingPerFlat": 0,
        "repaymentPerFlat": 0
      }

      console.log(this.debts)
    },

    deleteDebt: function(key) {
      if (key.startsWith('new')){
        delete this.debts[key];
      }
      else {
        this.debts['deleted' + key] = this.debts[key];
        delete this.debts[key];
      }
    },

    getDebts: function() {
      axios.get("/getAllDebts")
        .then((response) => {
          this.debts = response.data
        })
    },

    updateDebts: function() {
      axios.patch("/updateDebts", this.debts)
    }
  },

  created: function() {
    this.getConfig();
    this.getDebts();
  },

  mounted: function() {

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
}

.settingsColumn {
  width: 100%;
  display: flex;
  flex-flow: column nowrap;
  align-items: center;
  justify-content: flex-start;
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
}

</style>
