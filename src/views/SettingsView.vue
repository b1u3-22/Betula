<template>
    <div class="settings">
        <div class="settingsSaveButtonContainer">
            <div class="settingsSaveButtonIcon"></div>
            <div class="settingsSaveButton"></div>
        </div>
        <div class="settingsContentContainer">
            <BigTitle smallTextStyle="font-size: 0.8rem" bigTextStyle="font-size: 2.8rem" smallText="Obecné" bigText="Základní informace" side="false" />
            <form class="settingsForm">
                <template v-for="(item, index) in basicInfo" :key="item.property">
                    <div class="settingsRowContainer">
                        <label class="settingsLabel" :for="item.property">{{ item.name }}</label>
                        <input class="settingsInput" type="text" :id="item.property" :name="item.property" :placeholder="item.oldValue" v-model="basicInfo[index].newValue"/>
                    </div>
                </template>
            </form>
        </div>
        <div class="settingsContentContainer">
            <BigTitle smallTextStyle="font-size: 0.8rem" bigTextStyle="font-size: 2.8rem" smallText="Finance" bigText="Základní informace" side="false" />
            <form class="settingsForm">
                <template v-for="(item, index) in financeInfo" :key="item.property">
                    <div class="settingsRowContainer">
                        <label class="settingsLabel" :for="item.property">{{ item.name }}</label>
                        <input class="settingsInput" type="text" :id="item.property" :name="item.property" :placeholder="item.oldValue" v-model="basicInfo[index].newValue"/>
                    </div>
                </template>
            </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import BigTitle from '@/components/BigTitle.vue';
  // @ is an alias to /src
  
  export default {
    name: 'SettingsView',
    components: {
    BigTitle
},
    data: function() {
      return {
        basicInfo: [],
        financeInfo: []
      }
    },
    methods: {
    },
    mounted: function() {
    },
    created: function() {
        axios
        .get("http://127.0.0.1:5000/getGeneralInfo")
        .then((response) => {
            for (const [key, value] of Object.entries(response.data)){
                this.basicInfo.push({property: key, name: value.name, oldValue: value.text, newValue: ""})
            }

            console.log(this.basicInfo[0])
        });

        axios
        .get("http://127.0.0.1:5000/getFinancialsGeneral")
        .then((response) => {
            for (const [key, value] of Object.entries(response.data)){
                this.financeInfo.push({property: key, name: value.name, oldValue: value.text, newValue: ""})
            }

            console.log(this.financeInfo[0])
        });
    },
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
    display: flex;
    flex-flow: column nowrap;
    justify-content: flex-start;
    align-items: center;

    .settingsContentContainer {
        display: flex;
        flex-flow: column nowrap;
        width: 80%;
        padding: 3% 5%;
        justify-content: flex-start;
        align-items: center;
        box-shadow: 10px 10px 40px #D8D8D8;
        margin-bottom: 5%;

        .settingsForm {
            display: flex;
            flex-flow: column nowrap;
            align-items: center;
            justify-content: flex-start;
            width: 100%;

            .settingsRowContainer {
                display: flex;
                flex-flow: row nowrap;
                align-items: center;
                justify-content: space-between;
                width: 100%;
                border-bottom: 1px solid #D8D8D8;

                .settingsLabel {
                    font-weight: 400;
                    font-size: 1.2rem;
                    text-align: left;
                }

                .settingsInput {
                    border: none;
                    border-bottom: solid 2px $background-dark;
                    background-color: $background-light;
                    max-width: 30%;
                    width: 500px;
                    color: $background-dark;
                    font-size: 1.125rem;
                    font-weight: 500;
                    margin: 10px 0;
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
            }
        }
    }
  }
  
  @media (max-width: 600px){

  }
  
  
  </style>