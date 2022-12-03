<template>
  <div v-if="config.financeSection" class="dashboard" id="top">
    <div class="dashboardAddPostButton" @click="this.$router.push('add-post')">
      <img class="dashboardAddPostButtonIcon" :src="require('@/assets/icons/plus.svg')"/>
      <div class="dashboardAddPostButtonText">Přidat příspěvek</div>
    </div>
    <div class="dashboardMainContainer">
      <div v-if="config.financeSection.visible" class="dashboardFinancialContainer">
        <div class="dashboardFinancialHeaderContainer">
          <div class="dashboardFinancialButtonsContainer">
            <img :src="require(`@/assets/icons/arrow.svg`)" class="dashboardFinancialRollButton" :class="{dashboardFinancialButtonRollUp: financialRolledUp, dashboardFinancialButtonRollDown: !financialRolledUp}" @click="financialRolledUp = !financialRolledUp" />
          </div>
          <div :class="{dashboardFinanctialQuickInfoShowed: financialRolledUp, dashboardFinanctialQuickInfoHidden: !financialRolledUp}" class="dashboardFinancialQuickInfo">
            <div class="dashboardFinancialQuickInfoContentContainer">
              <label>Zůstatek na účtu</label>
              <h4>{{ config.financeSection.balance }}</h4>
            </div>
            <div v-if="remainingTotalDebt !== 0 && config.financeSection.debts.visible" class="dashboardFinancialQuickInfoContentContainer dashboardNoMobile">
              <label>Zbývající dluh</label>
              <h4> {{ remainingTotalDebt }} </h4>
            </div>
            <div v-if="monthlyTotalRepaymentPerFlat !== 0 && config.financeSection.debts.visible" class="dashboardFinancialQuickInfoContentContainer dashboardNoMobile">
              <label>Splátka na byt</label>
              <h4>{{ monthlyTotalRepaymentPerFlat }}</h4>
            </div>
          </div>
        </div>
        <div class="dashboardFinancialHelperContainer " :class="{dashboardFinancialRollUp: financialRolledUp, dashboardFinancialRollDown: !financialRolledUp}">
          <div class="dashboardFinancialSubContainer">
            <h3>Družstevní účet</h3>
            <div class="dashboardFinancialContentContainer">
              <div class="dashboardFinancialLine" />
              <div class="dashboardFinancialTextContainer">
                <div class="dashboardFinancialPartContainer">
                  <label>Číslo účtu</label>
                  <h5>{{ config.financeSection.accountNumber }}</h5>
                </div>
                <div class="dashboardFinancialPartContainer">
                  <label>Zůstatek na účtu</label>
                  <h5>{{ config.financeSection.balance }}</h5>
                </div>
              </div>
            </div>
            <div class="dashboardFinancialDocumentContainer">
              <ButtonLink link="/futurepdf" target="_blank">Uzávěrka</ButtonLink>
              <p>Účetní uzávěrka za rok {{ new Date().getFullYear() - 1 }}</p>
              <p><i>Zůstatek na účtu obsahuje i zálohy na vodné a stočné</i></p>
            </div>
          </div>
          <div v-if="(!(Object.keys(debts).length === 0)) && config.financeSection.debts.visible" class="dashboardFinancialSubContainer">
            <h3>Půjčky</h3>
            <div class="dashboardFinancialDebtContainer">
              <template v-for="debt in debts" :key="debt">
                <div class="dashboardFinancialContentContainer">
                  <div class="dashboardFinancialLine" />
                  <div class="dashboardFinancialTextContainer">
                    <div class="dashboardFinancialPartContainer">
                      <label>Čerpaná částka</label>
                      <h5>{{ debt.total }}</h5>
                    </div>
                    <div class="dashboardFinancialPartContainer">
                      <label>Zbývající částka</label>
                      <h5 class="dashboardFinancialContentText">{{ debt.remaining }}</h5>
                    </div>
                    <div class="dashboardFinancialPartContainer">
                      <label>Zbývající částka na byt</label>
                      <h5 class="dashboardFinancialContentText">{{ debt.remainingPerFlat }}</h5>
                    </div>
                    <div class="dashboardFinancialPartContainer">
                      <label>Měsíční splátka na byt</label>
                      <h5>{{ debt.repaymentPerFlat }}</h5>
                    </div>
                  </div>
                </div>
              </template>
            </div>
          </div>
        </div>
      </div>
      <div class="dashboardContentContainer">
        <template v-for="(item, index) in posts" :key="item.postID">
          <ContentCard :id="'post' + index" :title="item.postTitle" :timestamp="item.timestamp">{{item.postText}}</ContentCard>
        </template>
      </div>
    </div>
  </div>
</template>
<script>
import ContentCard from '@/components/ContentCard.vue';
import ButtonLink from '@/components/ButtonLink.vue';
import axios from 'axios';

export default {
  name: 'DashboardView',
  props: {
    verified: {
      type: Boolean
    }
  },
  data: function() {
    return {
      financialRolledUp: true,
      debts: {},
      remainingTotalDebt: 0, 
      monthlyTotalRepaymentPerFlat: 0,
      posts: [],
      config: {}
    }
  },
  components: {
    ContentCard,
    ButtonLink,
},

  methods: {
  },

  created: function(){

    if (!this.$props.verified){
      this.$router.push("/login")
    }

    axios
      .get("/getAllDebts")
      .then((response) => {
        this.debts = response.data
        for (const value of Object.values(response.data)){
          this.remainingTotalDebt += value.remaining
          this.monthlyTotalRepaymentPerFlat += value.repaymentPerFlat
        }
      });

    axios
      .get("/getDashboardPageConfig")
      .then((response) => {
        this.config = response.data
      });
  },

  mounted: function(){
    window.scrollTo({top: 0, behavior: 'auto'});

    
  }
}


</script>
<style scoped lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap');
@import "@/assets/colors.scss";

h5 {
  margin-bottom: 15px;
}
.dashboard {
  padding: 90px 0 0 0;
  min-height: 74vh;
  margin: 0;
  overflow-x: hidden;

  .dashboardAddPostButton {
    position: fixed;
    bottom: 5px;
    left: 5px;
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

    .dashboardAddPosetButtonIcon {
      height: 50px;
    }

    .dashboardAddPostButtonText {
      font-weight: 700;
      color: $background-light;
      margin-left: 5px;
      font-size: 1.2rem;
    }
  }

  .dashboardMainContainer {
    display: flex;
    flex-flow: column nowrap;
    justify-content: flex-start;
    align-items: center;

    .dashboardFinancialContainer {
      display: flex;
      flex-flow: column nowrap;
      justify-content: space-evenly;
      align-items: flex-start;
      box-shadow: 10px 10px 40px #D8D8D8;
      padding: 3% 5%;
      width: 80%;

      .dashboardFinancialHeaderContainer {
        display: flex;
        flex-flow: row-reverse nowrap;
        justify-content: space-between;
        align-items: center;
        width: 100%;

        .dashboardFinancialButtonsContainer {
          display: flex;
          flex-flow: row nowrap;
          justify-content: flex-end;
          align-items: center;

          .dashboardFinancialRollButton {
            cursor: pointer;
            transition: all 220ms ease-in-out;
            margin: 0;
            border-radius: 50%;
            //box-shadow: 10px 10px 40px #D8D8D8;
          }
        }

        .dashboardFinancialQuickInfo {
          display: flex;
          flex-flow: row nowrap;
          justify-content: flex-start;
          align-items: center;
          transition: all 220ms ease-in-out;

          .dashboardFinancialQuickInfoContentContainer {
            display: flex;
            flex-flow: column nowrap;
            justify-content: flex-start;
            align-items: flex-start;
            margin: 0 50px 0 0;
          }
        }
      }

        .dashboardFinancialHelperContainer {
          display: flex;
          flex-flow: row nowrap;
          justify-content: space-evenly;
          align-items: flex-start;
          width: 100%;
          transition: all 220ms ease-in-out;
          //margin-top: -50px;
          //animation: dashboardFinancialRollAnimation 500ms ease-in-out reverse;

          .dashboardFinancialSubContainer {
          display: flex;
          flex-flow: column nowrap;
          justify-content: flex-start;
          align-items: flex-start;
          margin: 0 7% 0 0;

          .dashboardFinancialDocumentContainer {
            display: flex;
            flex-flow: column nowrap;
            align-items: flex-start;
            justify-content: flex-start;
            margin-top: 20%;
          }
          .dashboardFinancialDebtContainer {
            display: flex;
            flex-flow: row nowrap;
            justify-content: flex-start;
            align-items: flex-start;
          }

          .dashboardFinancialContentContainer {
            display: flex;
            flex-flow: row nowrap;
            justify-content: flex-start;
            align-items: stretch;
            margin: 0 5% 0 0;

            .dashboardFinancialLine {
              width: 6px;
              background-color: $primary;
              margin: 0 10px -15% 0;
            }

            .dashboardFinancialTextContainer {
              display: flex;
              flex-flow: column nowrap;
              justify-content: flex-start;
              align-items: flex-start;
              margin: 0 0 -25px 0;
              width: fit-content;
              //white-space: nowrap;

              .dashboardFinancialPartContainer {
                display: flex;
                flex-flow: column nowrap;
                align-items: flex-start;
                justify-content: flex-start;
              }
            }
          }
        }
      }
    }
  }
}

.dashboardContentContainer {
  display: flex;
  flex-flow: column nowrap;
  justify-content: flex-start;
  align-items: center;
  width: 100%;
}

.dashboardNoMobile {
  opacity: 1;
  display: flex;
}

.dashboardFinancialRollUp {
  max-height: 0vh;
  opacity: 0;
  display: none;
  visibility: collapse;
  margin-top: 0;
}

.dashboardFinancialRollDown {
  opacity: 1;
  max-height: 100vh;
  display: flex;
  margin-top: -50px;
}

.dashboardFinancialButtonRollUp {
  transform: rotate(0deg);
  margin-bottom: 50px;
}

.dashboardFinancialButtonRollDown {
  transform: rotate(180deg);
}

.dashboardFinanctialQuickInfoHidden {
  opacity: 0;
}

.dashboardFinanctialQuickInfoShowed {
  transition-delay: 220ms;
  opacity: 1;
}

@media (max-width: 600px) {
  .dashboard {
    .dashboardAddPostButton {
      border-radius: 50%;

      .dashboardAddPostButtonText {
        display: none;
      }
    }
    .dashboardMainContainer {
      .dashboardFinancialContainer {
        width: 100%;
        box-sizing: border-box;
        padding: 5%;

        .dashboardFinancialHeaderContainer {
          .dashboardFinancialQuickInfo {
            .dashboardNoMobile {
              display: none;
            }
          }
        }

        .dashboardFinancialHelperContainer {
          flex-flow: column nowrap;
          justify-content: center;

          .dashboardFinancialSubContainer {
            width: 100%;
            align-items: center;

            .dashboardFinancialDebtContainer {
              justify-content: space-evenly;
              width: 100%;
            }

            .dashboardFinancialContentContainer {
              justify-content: center;
              margin: 0;
              width: 30%;
              
              .dashboardFinancialLine {
                display: none;
              }

              .dashboardFinancialTextContainer {
                align-items: center;

                .dashboardFinancialPartContainer {
                  align-items: center;

                  .dashboardFinancialPartHeader {
                    text-align: center;
                  }
                }
              }
            }

            .dashboardFinancialDocumentContainer {
              margin-top: 5%;
              align-items: center;
            }
          }
        }
      }
    }
  }
}

</style>