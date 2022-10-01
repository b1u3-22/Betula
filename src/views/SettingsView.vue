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
        <div class="settingsContentContainer">
            <BigTitle smallTextStyle="font-size: 0.8rem" bigTextStyle="font-size: 2.8rem" smallText="Uživatelé" bigText="Přehled uživatelských účtů" side="false" />
            <form class="settingsForm">
                <TransitionGroup name="list">
                    <template v-for="(item, index) in accountInfo" :key="item.id">
                        <div class="settingsRowContainer settingRowContainerAnimation">
                            <div class="settingsUserAccountHelper">
                                <div class="settingsUserAccountColumn" style="margin-right: 20px">
                                    <label class="settingsLabelUserAccount" :for="'username' + index">Uživatelské jméno</label>
                                    <input class="settingsInputUserAccount" type="text" :id="'username' + index" name="username" :placeholder="item.oldUsername" v-model="accountInfo[index].newUsername"/>
                                </div>
                                <div class="settingsUserAccountColumn">
                                    <label class="settingsLabelUserAccount" :for="'password' + index">Heslo</label>
                                    <input class="settingsInputUserAccount" type="password" :id="'password' + index" name="password" placeholder="Uživatelské heslo" v-model="accountInfo[index].newPassword"/>
                                </div>
                            </div>
                            <div class="settingsUserAccountHelper" style="justify-content: flex-end">
                                <div class="settingsUserAccountToggles">
                                    <div class="settingsUserAccountToggle">
                                        <div class="settingsLabelUserAccount">Smazat</div>
                                        <img :src="require(`@/assets/icons/deleteForeverIcon.svg`)" class="settingUserAcountDelete" @click="deleteAccount(accountInfo[index].userId, index)" />
                                    </div>
                                    <div class="settingsUserAccountToggle">
                                        <label class="settingsLabelUserAccount">Aktivní</label>
                                        <input type="checkbox" class="settingsUserAccountToggleCheckbox" v-model="accountInfo[index].status" :disabled="accountInfo.length < 2"  />
                                        <div class="settingLabelAccountToggleCheckboxCosmetic"/>
                                    </div>
                                    <div class="settingsUserAccountToggle">
                                        <div class="settingsLabelUserAccount">Admin</div>
                                        <input type="checkbox" class="settingsUserAccountToggleCheckbox" v-model="accountInfo[index].admin" :disabled="accountInfo.length < 2" />
                                        <div class="settingLabelAccountToggleCheckboxCosmetic"/>
                                    </div>
                                </div>
                                <div class="settingsUserAccountColumn">
                                    <label class="settingsLabelUserAccount" :for="'email' + index">Emailová adresa</label>
                                    <input class="settingsInputUserAccount" type="email" :id="'email' + index" name="email" :placeholder="item.oldEmail" v-model="accountInfo[index].newEmail"/>
                                </div>
                            </div>
                        </div>
                    </template>
                </TransitionGroup>
                <div class="settingActionButtonContainer">
                    <ButtonAction @click="newAccount">Nový uživatel</ButtonAction>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import BigTitle from '@/components/BigTitle.vue';
import ButtonAction from '@/components/ButtonAction.vue';
  // @ is an alias to /src
  
  export default {
    name: 'SettingsView',
    components: {
    BigTitle,
    ButtonAction
},
    data: function() {
      return {
        basicInfo: [],
        financeInfo: [],
        accountInfo: [],
        accountInfoBackUp: [],

      }
    },
    methods: {
        deleteAccount: function(id, index) {

            if (this.accountInfo.length > 1){
                this.accountInfo.splice(index, 1);
                console.log(this.accountInfo)
            }

            else {
                this.$notify({
                    type: "error",
                    title: "Tento účet nelze smazat",
                    text: "V Systému musí být aspoň jeden uživatel"
                })
            }
        },

        newAccount: function() {
            let id = 0

            for (let account of this.accountInfo){
                if (account.userId > id) {
                    id = account.userId;
                }
            }

            this.accountInfo.push({
                newUsername: "",
                oldUsername: "Nový uživatel",
                oldPassword: "Heslo",
                newPassword: "",
                status: false,
                admin: false, 
                oldEmail: "Emailová adresa",
                newEmail: "",
                userId: id
            })
        
        }
    },
    watch:  {
        'accountInfo.length'(){
            if (this.accountInfo.length <= 1){
                this.accountInfo[0].admin = true;
                this.accountInfo[0].status = true;
            }
        }
    },
    mounted: function() {
    },
    created: function() {
        axios
        .get("http://127.0.0.1:5000/getGeneralInfo")
        .then((response) => {
            for (const [key, value] of Object.entries(response.data)){
                this.basicInfo.push({property: key,
                    name: value.name,
                    oldValue: value.text, 
                    newValue: ""
                })
            }
        });

        axios
        .get("http://127.0.0.1:5000/getFinancialsGeneral")
        .then((response) => {
            for (const [key, value] of Object.entries(response.data)){
                this.financeInfo.push({property: key, 
                    name: value.name, 
                    oldValue: value.text, 
                    newValue: ""
                })
            }
        });

        axios
        .get("http://127.0.0.1:5000/getAllUsers")
        .then((response) => {
            for (const [key, value] of Object.entries(response.data)){
                this.accountInfo.push({oldUsername: key, 
                    newUsername: "", 
                    oldPassword: value.password, 
                    newPassword: "", 
                    status: value.status === "active" ? true : false, 
                    admin: value.permissions === "admin" ? true : false,
                    oldEmail: value.email !== '' ? value.email : "Emailová adresa",
                    newEmail: "",
                    userId: value.id
                })
            }       
            this.accountInfoBackUp = this.accountInfo;
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
        //box-shadow: 10px 10px 40px #D8D8D8;
        margin-bottom: 5%;

        .settingsForm {
            display: flex;
            flex-flow: column nowrap;
            align-items: center;
            justify-content: flex-start;
            width: 100%;

            .settingActionButtonContainer {
                margin-top: 3%;
            }

            .settingRowContainerAnimation {
                animation: appear 220ms ease-in-out;
            }

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

                .settingsUserAccountHelper {
                    display: flex;
                    flex-flow: row nowrap;
                    align-items: stretch;
                    justify-content: flex-start;

                    .settingsUserAccountColumn {
                        display: flex;
                        flex-flow: column nowrap;
                        align-items: flex-start;
                        justify-content: flex-start;

                        .settingsLabelUserAccount {
                            font-weight: 700;
                            font-size: 1rem;
                            text-align: left;
                            color: $primary;
                            margin-top: 10px;
                        }

                        .settingsInputUserAccount {
                            border: none;
                            border-bottom: solid 2px $background-dark;
                            background-color: $background-light;
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

                    .settingsUserAccountToggles {
                        display: flex;
                        flex-flow: row nowrap;
                        justify-content: flex-end;
                        align-items: center;

                        .settingsUserAccountToggle {
                            display: flex;
                            flex-flow: column nowrap;
                            align-items: center;
                            justify-content: center;
                            margin-right: 20px;

                            .settingUserAcountDelete {
                                cursor: pointer;
                            }

                            .settingsLabelUserAccount {
                                margin-bottom: 5px;
                            }

                            .settingLabelAccountToggleCheckboxCosmetic {
                                z-index: 0;
                                height: 1.125rem;
                                width: 1.125rem;
                                margin: 0 0 0 0;
                                border-radius: 50%;
                                border: solid $primary 1px;
                            }

                            .settingsUserAccountToggleCheckbox {
                                z-index: 1;
                                height: 1.125rem;
                                width: 1.125rem;
                                margin-bottom: -1.125rem;
                                cursor: pointer;
                                opacity: 0;

                                &:checked ~ .settingLabelAccountToggleCheckboxCosmetic {
                                    background-color: $primary;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
  }

.list-enter-active {
    transition: all 220ms ease-in-out;
}

.list-leave-active {
    transition: all 220ms ease-in-out;
}

.list-enter-from {
    opacity: 0;
    transform: translateX(50px);
    max-height: 0px;
}

.list-leave-to {
    opacity: 0;
    transform: translateX(50px);
    max-height: 0px;
}

.list-enter-to {
    opacity: 1;
    transform: translateX(0px);
    max-height: 250px
}

.list-leave-from {
    opacity: 1;
    transform: translateX(0px);
    max-height: 250px
}

@keyframes appear {
    from {
        opacity: 0;
        transform: translateX(50px);
        max-height: 0;
    }

    to {
        opacity: 1;
        transform: translateX(0px);
        max-height: 250px
    }
}
  
  @media (max-width: 600px){

  }
  
  
  </style>