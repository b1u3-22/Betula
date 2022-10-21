<template>
    <div class="settings">
        <div class="settingsSaveButtonContainer" @click="saveAll">
            <img class="settingsSaveButtonIcon" :src="require('@/assets/icons/save.svg')" />
            <div class="settingsSaveButtonText">Uložit všechny změny</div>
        </div>
        <div class="settingsContentContainer" id="settings-general">
            <BigTitle smallTextStyle="font-size: 0.8rem" bigTextStyle="font-size: 2.8rem" smallText="Obecné" bigText="Základní informace" side="false" />
            <form class="settingsForm">
                <template v-for="(item, index) in basicInfo" :key="item.property">
                    <div class="settingsRowContainer">
                        <label class="settingsLabelSimple" :for="item.property">{{ item.name }}</label>
                        <input class="settingsInput" type="text" :id="item.property" :name="item.property" :placeholder="item.oldValue" v-model="basicInfo[index].newValue"/>
                    </div>
                </template>
            </form>
        </div>
        <div class="settingsContentContainer" id="settings-finance">
            <BigTitle smallTextStyle="font-size: 0.8rem" bigTextStyle="font-size: 2.8rem" smallText="Finance" bigText="Základní informace" side="false" />
            <form class="settingsForm">
                <template v-for="(item, index) in financeInfo" :key="item.property">
                    <div class="settingsRowContainer">
                        <label class="settingsLabelSimple" :for="item.property">{{ item.name }}</label>
                        <input class="settingsInput" type="text" :id="item.property" :name="item.property" :placeholder="item.oldValue" v-model="basicInfo[index].newValue"/>
                    </div>
                </template>
            </form>
        </div>
        <div class="settingsContentContainer">
            <BigTitle smallTextStyle="font-size: 0.8rem" bigTextStyle="font-size: 2.8rem" smallText="Finance" bigText="Půjčky" side="false" />
            <form class="settingsForm">
                <TransitionGroup name="list">
                    <template v-for="(item, index) in debtsInfo" :key="item.debtId">
                        <div class="settingsRowContainer">
                            <div class="settingsSide">
                                <div class="settingsColumn" style="margin-right: 20px">
                                    <label class="settingsLabel" :for="'total_debt' + index">Čerpaná částka</label>
                                    <input class="settingsInput" type="number" :id="'total_debt' + index" name="total_debt" :placeholder="item.totalDebtOld" v-model="debtsInfo[index].totalDebtNew"/>
                                </div>
                                <div class="settingsColumn">
                                    <label class="settingsLabel" :for="'remaining_debt' + index">Zbývající částka</label>
                                    <input class="settingsInput" type="number" :id="'remaining_debt' + index" name="remaining_debt" :placeholder="item.remainingDebtOld" v-model="debtsInfo[index].remainingDebtNew"/>
                                </div>
                            </div>
                            <div class="settingsSide">
                                <div class="settingsColumn" style="margin-right: 20px">
                                    <label class="settingsLabel" :for="'remaining_debt_per_flat' + index">Částka na byt</label>
                                    <input class="settingsInput" type="number" :id="'remaining_debt_per_flat' + index" name="remaining_debt_per_flat" :placeholder="item.remainingDebtPerFlatOld" v-model="debtsInfo[index].remainingDebtPerFlatNew"/>
                                </div>
                                <div class="settingsColumn">
                                    <label class="settingsLabel" :for="'repainment_per_flat' + index">Splátka na byt</label>
                                    <input class="settingsInput" type="number" :id="'repainment_per_flat' + index" name="text" :placeholder="item.repaimentPerFlatOld" v-model="debtsInfo[index].repaimentPerFlatNew"/>
                                </div>
                                <div class="settingsButtons">
                                    <div class="settingsButton">
                                        <label class="settingsLabel">Smazat</label>
                                        <img :src="require(`@/assets/icons/deleteForeverIcon.svg`)" class="settingsButtonIcon" @click="deleteDebt(debtsInfo[index].debtId, index)" />
                                    </div>
                                </div>
                            </div>
                        </div>
                    </template>
                </TransitionGroup>
                <div class="settingActionButtonContainer">
                    <ButtonAction @click="newDebt">Nová půjčka</ButtonAction>
                </div>
            </form>
        </div>
        <div class="settingsContentContainer" id="settings-users">
            <BigTitle smallTextStyle="font-size: 0.8rem" bigTextStyle="font-size: 2.8rem" smallText="Uživatelé" bigText="Přehled uživatelských účtů" side="false" />
            <form class="settingsForm" autocomplete="off">
                <TransitionGroup name="list">
                    <template v-for="(item, index) in accountInfo" :key="item.userId">
                        <div class="settingsRowContainer settingRowContainerAnimation">
                            <div class="settingsSide">
                                <div class="settingsColumn" style="margin-right: 20px">
                                    <label class="settingsLabel" :for="'username' + index">Uživatelské jméno</label>
                                    <input class="settingsInput" type="text" :id="'username' + index" name="username" :placeholder="item.oldUsername" v-model="accountInfo[index].newUsername"/>
                                </div>
                                <div class="settingsColumn">
                                    <label class="settingsLabel" :for="'password' + index">Heslo</label>
                                    <input class="settingsInput" type="password" :id="'password' + index" name="password" placeholder="Uživatelské heslo" v-model="accountInfo[index].newPassword"/>
                                </div>
                            </div>
                            <div class="settingsSide" style="justify-content: flex-end">
                                <div class="settingsButtons">
                                    <div class="settingsButton">
                                        <label class="settingsLabel">Smazat</label>
                                        <img :src="require(`@/assets/icons/deleteForeverIcon.svg`)" class="settingsButtonIcon" @click="deleteAccount(accountInfo[index].userId, index)" />
                                    </div>
                                    <div class="settingsButton">
                                        <label class="settingsLabel">Aktivní</label>
                                        <input type="checkbox" class="settingsCheckbox" v-model="accountInfo[index].status" true-value="active" false-value="blocked" :disabled="accountInfo.length < 2"  />
                                        <div class="settingsCheckboxCosmetic"/>
                                    </div>
                                    <div class="settingsButton">
                                        <label class="settingsLabel">Admin</label>
                                        <input type="checkbox" class="settingsCheckbox" v-model="accountInfo[index].admin" true-value="admin" false-value="basic" :disabled="accountInfo.length < 2" />
                                        <div class="settingsCheckboxCosmetic"/>
                                    </div>
                                </div>
                                <div class="settingsColumn">
                                    <label class="settingsLabel" :for="'email' + index">Emailová adresa</label>
                                    <input class="settingsInput" type="email" :id="'email' + index" name="email" :placeholder="item.oldEmail" v-model="accountInfo[index].newEmail"/>
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
        <div class="settingsContentContainer" id="settings-images">
            <BigTitle smallTextStyle="font-size: 0.8rem" bigTextStyle="font-size: 2.8rem" smallText="Galerie" bigText="Správa fotek" side="false" />
            <form class="settingsForm">
                <template v-for="(item, index) in picturesInfo" :key="item.pictureID">
                    <div class="settingsRowContainer">
                        <div class="settingsSide">
                            <div class="settingsColumn">
                                <img :src="item.link" class="settingsImagesPreview"/>
                            </div>
                            <div class="settingsColumn">
                                <label class="settingsLabel" :for="'pictureDesc' + index">Popis</label>
                                <input class="settingsInput" type="text" :id="'pictureDesc' + index" :name="'pictureDesc' + index" v-model="picturesInfo[index].newDescription" :placeholder="item.oldDescription"/>
                            </div>
                        </div>
                        <div class="settingsButtons">
                            <div class="settingsButton">
                                <label class="settingsLabel">Smazat</label>
                                <img class="settingsButtonIcon" :src="require('@/assets/icons/deleteForeverIcon.svg')" />
                            </div>
                            <div class="settingsButton">
                                <label class="settingsLabel">Na hlavní stránce</label>
                                <input type="checkbox" class="settingsCheckbox" true-value="true" false-value="" v-model="picturesInfo[index].onMainPage" />
                                <div class="settingsCheckboxCosmetic" />
                            </div>
                            <div class="settingsButton">
                                <label class="settingsLabel">Na pozadí</label>
                                <input type="checkbox" class="settingsCheckbox" true-value="true" false-value="" v-model="picturesInfo[index].isBackground" />
                                <div class="settingsCheckboxCosmetic" />
                            </div>
                        </div>
                    </div>
                </template>
            </form>
            <FileUpload @uploadFiles="uploadImages" style="margin-top: 5%;"></FileUpload>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import BigTitle from '@/components/BigTitle.vue';
import ButtonAction from '@/components/ButtonAction.vue';
import { getCurrentInstance } from 'vue';
import FileUpload from '@/components/FileUpload.vue';
  // @ is an alias to /src
  
  export default {
    name: 'SettingsView',
    components: {
    BigTitle,
    ButtonAction,
    FileUpload
},
    data: function() {
      return {
        basicInfo: [],
        financeInfo: [],
        accountInfo: [],
        accountInfoBackUp: [],
        debtsInfo: [],
        debtsInfoBackUp: [],
        picturesInfo: [], 
        picturesInfoBackUp: []
      }
    },
    methods: {
        getGeneralInfo: function(){
            axios
            .get("http://127.0.0.1:5000/getGeneralInfo")
            .then((response) => {
                this.basicInfo.length = 0;
                for (const [key, value] of Object.entries(response.data)){
                    this.basicInfo.push({
                        property: key,
                        name: value.name,
                        oldValue: value.text, 
                        newValue: ""
                    })
                }
            });
        },

        getFinancialInfo: function(){
            axios
            .get("http://127.0.0.1:5000/getFinancialsGeneral")
            .then((response) => {
                this.financeInfo.length = 0;
                for (const [key, value] of Object.entries(response.data)){
                    this.financeInfo.push({
                        property: key, 
                        name: value.name, 
                        oldValue: value.text, 
                        newValue: ""
                    })
                }
            });
        },

        getUserInfo: function(){
            axios
            .get("http://127.0.0.1:5000/getAllUsers")
            .then((response) => {
                this.accountInfo.length = 0;
                this.accountInfoBackUp.length = 0;
                for (const [key, value] of Object.entries(response.data)){
                    this.accountInfo.push({
                        oldUsername: key, 
                        newUsername: "", 
                        oldPassword: value.password, 
                        newPassword: "", 
                        status: value.status, 
                        admin: value.permissions,
                        oldEmail: value.email !== '' ? value.email : "Emailová adresa",
                        newEmail: "",
                        userId: value.id
                    })
                }       
                this.accountInfoBackUp = this.accountInfo.slice();
            });
        },

        getDebtsInfo: function(){
            axios
            .get("http://127.0.0.1:5000/getAllDebts")
            .then((response) => {
                this.debtsInfo.length = 0;
                this.debtsInfoBackUp.length = 0;
                for (const [key, value] of Object.entries(response.data)){
                    this.debtsInfo.push({
                        totalDebtOld: value.total_debt,
                        totalDebtNew: "",
                        remainingDebtOld: value.remaining_debt,
                        remainingDebtNew: "",
                        remainingDebtPerFlatOld: value.remaining_debt_per_flat,
                        remainingDebtPerFlatNew: "",
                        repaimentPerFlatOld: value.repainment_per_flat,
                        repaimentPerFlatNew: "",
                        debtId: key
                    })
                }       
                this.debtsInfoBackUp = this.debtsInfo.slice();
            });
        },

        getImagesInfo: function(){
            axios
            .get("http://127.0.0.1:5000/getAllPictures")
            .then((response) => {
                this.picturesInfo.length = 0;
                this.picturesInfoBackUp.length = 0;
                for (const [key, value] of Object.entries(response.data)){
                    this.picturesInfo.push({
                        pictureID: key,
                        link: value.link,
                        oldDescription: value.description,
                        newDescription: "",
                        isBackground: value.is_background,
                        onMainPage: value.on_mainpage
                    })
                }       
                this.picturesInfoBackUp = this.picturesInfo.slice();
            });
        },

        getAll: function(){
            this.getGeneralInfo();
            this.getFinancialInfo();
            this.getDebtsInfo();
            this.getImagesInfo();
        },

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

            for (let user of this.accountInfo){
                if (user.userId > id) {
                    id = user.userId;
                }
            }

            id += 1000

            this.accountInfo.push({
                newUsername: "",
                oldUsername: "Nový uživatel",
                oldPassword: "Heslo",
                newPassword: "",
                status: "blocked",
                admin: "basic", 
                oldEmail: "Emailová adresa",
                newEmail: "",
                userId: id
            })
        
        },

        deleteDebt: function(id, index){
            this.debtsInfo.splice(index, 1)
        },

        newDebt: function() {
            let id = 0

            for (let debt of this.debtsInfo){
                if (debt.debtId > id) {
                    id = parseInt(debt.debtId);
                }
            }

            id += 1000

            this.debtsInfo.push({
                totalDebtOld: "Nová půjčka",
                totalDebtNew: "",
                remainingDebtOld: "Zbývá doplatit",
                remainingDebtNew: "",
                remainingDebtPerFlatOld: "Částka na byt",
                remainingDebtPerFlatNew: "",
                repaimentPerFlatOld: "Splátka na byt",
                repaimentPerFlatNew: "",
                debtId: id
            })
        },

        saveGeneralInfo(){
            let basicInfoToSave = {}

            for (let info of this.basicInfo){
                if (info.newValue !== "" && info.newValue !== info.oldValue){
                    basicInfoToSave[info.property] = info.newValue;
                }
            }

            axios.patch("http://127.0.0.1:5000/patchGeneralInfo", basicInfoToSave)
        },

        saveFinancialInfo(){
            let financeInfoToSave = {}

            for (let info of this.financeInfo) {
                if (info.newValue !== "" && info.newValue !== info.oldValue){
                    financeInfoToSave[info.property] = info.newValue;
                }
            }

            axios.patch("http://127.0.0.1:5000/patchFinancialsGeneral", financeInfoToSave)
        },
        saveUserInfo(){
            let userChanges = {}
            let userFound = false;

            for (let user of this.accountInfoBackUp) {
                userFound = false;
                for (let newUser of this.accountInfo) {
                    if (user.userId === newUser.userId){
                        userFound = true;
                        break;
                    }
                }
                if (!userFound){
                    userChanges[user.userId] = "deleted";
                }
            }

            // Update all users
            for (let user of this.accountInfo){
                userChanges[user.userId] = {
                    username: user.newUsername !== "" && user.newUsername !== user.oldUsername ? user.newUsername : user.oldUsername,
                    password: user.newPassword !== "" && user.newPassword !== user.oldPassword ? user.newPassword : user.oldPassword,
                    permissions: user.admin,
                    status: user.status,
                    email: user.newEmail !== "" && user.newEmail !== user.oldEmail ? user.newEmail : user.oldEmail === "Emailová adresa" ? "" : user.oldEmail
                }
            }

            axios.patch("http://127.0.0.1:5000/patchUsers", userChanges)
        },

        saveDebtsInfo(){
            let debtChanges = {}
            let debtFound = false;

            for (let debt of this.debtsInfoBackUp) {
                debtFound = false;
                for (let newDebt of this.debtsInfo) {
                    if (debt.debtId === newDebt.debtId){
                        debtFound = true;
                        break;
                    }
                }
                if (!debtFound){
                    debtChanges[debt.debtId] = "deleted";
                }
            }

            for (let debt of this.debtsInfo){
                debtChanges[debt.debtId] = {
                    total_debt: debt.totalDebtNew !== "" && debt.totalDebtNew !== debt.totalDebtOld ? debt.totalDebtNew : debt.totalDebtOld,
                    remaining_debt: debt.remainingDebtNew !== "" && debt.remainingDebtNew !== debt.remainingDebtOld ? debt.remainingDebtNew : debt.remainingDebtOld,
                    remaining_debt_per_flat: debt.remainingDebtPerFlatNew !== "" && debt.remainingDebtPerFlatNew !== debt.remainingDebtPerFlatOld ? debt.remainingDebtPerFlatNew : debt.remainingDebtPerFlatOld,
                    repainment_per_flat: debt.repaimentPerFlatNew !== "" && debt.repaimentPerFlatNew !== debt.repaimentPerFlatOld ? debt.repaimentPerFlatNew : debt.repaimentPerFlatOld
                }
            }

            axios.patch("http://127.0.0.1:5000/patchDebts", debtChanges)
        },

        saveImagesInfo(){

        },

        saveAll: function() {
            try {
                this.saveGeneralInfo();
                this.saveFinancialInfo();
                this.saveDebtsInfo();
                this.saveImagesInfo();
            
                this.$notify({
                    type: "success",
                    title: "Uloženo",
                    text: "Všechna nastavení byla uložena"
                })

                //this.$router.push("/dashboard")

                setTimeout(() => {
                    this.getAll()
                }, 50)
            }
            catch {
                this.$notify({
                    type: "error",
                    title: "Chyba",
                    text: "Při ukládání došlo k chybě"
                })
            }
        },

        uploadImages: function(files){
            for (let file of files){
                axios.put("http://127.0.0.1:5000/uploadNewImages", file, {
                    headers: {
                        "Content-Type": file.type
                    }
                })
                .then(() => {
                    this.getAllPictures();
                })
            }
        }
    },
    watch:  {
        'accountInfo.length'(){
            if (this.accountInfo.length <= 1){
                this.accountInfo[0].admin = "admin";
                this.accountInfo[0].status = "active";
            }
        },

        $route: function(to){
            let path = to.path.replace('/', '')
            path === '' ? path = 'home' : '';
            if (path.includes('settings')){
                document.getElementById(path).scrollIntoView({behavior: "smooth"})
            }
        }
    },
    created: function() {
        if (!getCurrentInstance().parent.ctx.$parent.verified){
            this.$router.push("/login")
        }
        else if (!getCurrentInstance().parent.ctx.$parent.permissions){
            this.$router.push("/dashboard")
        }
    },
    mounted: function() {
        window.scrollTo({top: 0, behavior: 'auto'});
        this.getGeneralInfo();
        this.getFinancialInfo();
        this.getUserInfo();
        this.getDebtsInfo();
        this.getImagesInfo();
    },
  }
</script>
  
  <style scoped lang="scss">
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap');
  @import "@/assets/colors.scss";
  
.settingsRowContainer {
    display: flex;
    flex-flow: row nowrap;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    border-bottom: 1px solid #D8D8D8;
    transition: all 220ms ease-in-out;
}

.settingRowContainerAnimation {
    animation: appear 220ms ease-in-out;
    transition: all 220ms ease-in-out;
}

.settingsForm {
    display: flex;
    flex-flow: column nowrap;
    align-items: center;
    justify-content: flex-start;
    width: 100%;
}

.settingsContentContainer {
    display: flex;
    flex-flow: column nowrap;
    width: 80%;
    padding: 3% 5%;
    justify-content: flex-start;
    align-items: center;
    //box-shadow: 10px 10px 40px #D8D8D8;
    margin-bottom: 5%;
}

.settingsSide {
    display: flex;
    flex-flow: row nowrap;
    align-items: stretch;
    justify-content: flex-start;
}

.settingsColumn {
    display: flex;
    flex-flow: column nowrap;
    align-items: flex-start;
    justify-content: center;
}

.settingsLabelSimple {
    font-weight: 400;
    color: $background-dark;
    font-size: 1.2rem;
}

.settingsInput {
    width: 200px;
    max-width: 20vw;
}

.settingsButtons {
    display: flex;
    flex-flow: row nowrap;
    justify-content: flex-start;
    align-items: flex-start;

    .settingsButton {
        display: flex;
        flex-flow: column nowrap;
        align-items: center;
        justify-content: flex-start;
        margin: 0 10px;

        .settingsButtonText {
            font-weight: 700;
            color: $primary;
            margin-bottom: 5px;
        }

        .settingsButtonIcon {
            margin: 0;
            cursor: pointer;
        }
    }
}

.settingsCheckboxCosmetic {
    z-index: 0;
    height: 1.125rem;
    width: 1.125rem;
    margin: 0 0 0 0;
    border-radius: 50%;
    border: solid $primary 3px;
}

.settingsCheckbox {
    z-index: 1;
    height: 1.125rem;
    width: 1.125rem;
    margin-bottom: -1.125rem;
    cursor: pointer;
    opacity: 0;

    &:checked ~ .settingsCheckboxCosmetic {
        background-color: $primary;
    }
}

.settings {
padding: 90px 0 0 0;
min-height: 74vh;
margin: 0;
overflow-x: hidden;
display: flex;
flex-flow: column nowrap;
justify-content: flex-start;
align-items: center;

}

.settingsSaveButtonContainer {
    position: fixed;
    bottom: 5px;
    left: 5px;
    height: 50px;
    background-color: $primary;
    display: flex;
    flex-flow: row nowrap;
    padding: 15px;
    justify-content: center;
    align-items: center;
    box-shadow: 0px 10px 15px rgba(0, 0, 0, 0.25);
    z-index: 999999;
    box-sizing: border-box;
    cursor: pointer;

    .settingsSaveIcon {
        height: 50px;
    }

    .settingsSaveButtonText {
        font-weight: 700;
        color: $background-light;
        margin-left: 5px;
        font-size: 1.2rem;
    }
}

.settingsImagesPreview {
    height: 75px;
    width: 75px;    
    object-fit: cover;
}

.list-enter-active {
    transition: all 220ms ease-in-out;
}

.list-leave-active {
    transition: all 220ms ease-in-out;
}

.list-move {
    transition: all 220ms ease-in-out !important;
}

.list-enter-from {
    opacity: 0;
    transform: translate(50px, 0);
    max-height: 0px;
}

.list-leave-to {
    opacity: 0;
    transform: translate(50px, 0);
    max-height: 0px;
}

.list-enter-to {
    opacity: 1;
    transform: translate(0px, 0);
    max-height: 250px
}

.list-leave-from {
    opacity: 1;
    transform: translate(0px, 0);
    max-height: 250px
}

@keyframes appear {
    from {
        opacity: 0;
        transform: translate(50px, 0);
        max-height: 0;
    }

    to {
        opacity: 1;
        transform: translate(0px, 0);
        max-height: 250px
    }
}

@media (max-width: 600px){

    .settingsSaveButtonContainer {
        border-radius: 50%;

        .settingsSaveButtonText {
            visibility: collapse;
            display: none;
        }
    }
    
}
  
  
</style>