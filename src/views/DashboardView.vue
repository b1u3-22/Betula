<template>
  <div class="dashboard" id="top">
    <div class="dashboardMainContainer">
      <div class="dashboardFinancialContainer">
        <div class="dashboardFinancialHeaderContainer">
          <div class="dashboardFinancialButtonsContainer">
            <img :src="require(`@/assets/icons/circleArrowIcon.svg`)" class="dashboardFinancialRollButton" :class="{dashboardFinancialButtonRollUp: financialRolledUp, dashboardFinancialButtonRollDown: !financialRolledUp}" @click="financialRolledUp = !financialRolledUp" />
          </div>
          <div :class="{dashboardFinanctialQuickInfoShowed: financialRolledUp, dashboardFinanctialQuickInfoHidden: !financialRolledUp}" class="dashboardFinancialQuickInfo">
            <div class="dashboardFinancialQuickInfoContentContainer">
              <div class="dashboardFinancialQuickInfoTitle">Zůstatek na účtu</div>
              <div class="dashboardFinancialQuickInfoText">{{ balance }}</div>
            </div>
            <div v-if="remainingTotalDebt !== 0" class="dashboardFinancialQuickInfoContentContainer dashboardNoMobile">
              <div class="dashboardFinancialQuickInfoTitle">Zbývající dluh</div>
              <div class="dashboardFinancialQuickInfoText"> {{ remainingTotalDebt }} </div>
            </div>
            <div v-if="monthlyTotalRepainmentPerFlat !== 0" class="dashboardFinancialQuickInfoContentContainer dashboardNoMobile">
              <div class="dashboardFinancialQuickInfoTitle">Splátka na byt</div>
              <div class="dashboardFinancialQuickInfoText">{{ monthlyTotalRepainmentPerFlat }}</div>
            </div>
          </div>
        </div>
        <div class="dashboardFinancialHelperContainer " :class="{dashboardFinancialRollUp: financialRolledUp, dashboardFinancialRollDown: !financialRolledUp}">
          <div class="dashboardFinancialSubContainer">
            <h1 class="dashboardFinancialHeader">Družstevní účet</h1>
            <div class="dashboardFinancialContentContainer">
              <div class="dashboardFinancialLine" />
              <div class="dashboardFinancialTextContainer">
                <div class="dashboardFinancialPartContainer">
                  <h2 class="dashboardFinancialPartHeader">Číslo účtu</h2>
                  <p class="dashboardFinancialContentText">{{ accountNumber }}</p>
                </div>
                <div class="dashboardFinancialPartContainer">
                  <h2 class="dashboardFinancialPartHeader">Zůstatek na účtu</h2>
                  <p class="dashboardFinancialContentText">{{ balance }}</p>
                </div>
              </div>
            </div>
            <div class="dashboardFinancialDocumentContainer">
              <ButtonLink link="/futurepdf" target="_blank">Uzávěrka</ButtonLink>
              <p class="dashboardFinancialDocumentText">Účetní uzávěrka za rok {{ new Date().getFullYear() - 1 }}</p>
            </div>
          </div>
          <div v-if="debts.length" class="dashboardFinancialSubContainer">
            <h1 class="dashboardFinancialHeader">Půjčky</h1>
            <div class="dashboardFinancialDebtContainer">
              <template v-for="debt in debts" :key="debt">
                <div class="dashboardFinancialContentContainer">
                  <div class="dashboardFinancialLine" />
                  <div class="dashboardFinancialTextContainer">
                    <div class="dashboardFinancialPartContainer">
                      <h2 class="dashboardFinancialPartHeader">Čerpaná částka</h2>
                      <p class="dashboardFinancialContentText">{{ debt.totalDebt }}</p>
                    </div>
                    <div class="dashboardFinancialPartContainer">
                      <h2 class="dashboardFinancialPartHeader">Zbývající částka</h2>
                      <p class="dashboardFinancialContentText">{{ debt.remainingDebt }}</p>
                    </div>
                    <div class="dashboardFinancialPartContainer">
                      <h2 class="dashboardFinancialPartHeader">Zbývající částka na byt</h2>
                      <p class="dashboardFinancialContentText">{{ debt.remainingDebtPerFlat }}</p>
                    </div>
                    <div class="dashboardFinancialPartContainer">
                      <h2 class="dashboardFinancialPartHeader">Měsíční splátka na byt</h2>
                      <p class="dashboardFinancialContentText">{{ debt.repaimentPerFlat }}</p>
                    </div>
                  </div>
                </div>
              </template>
            </div>
          </div>
        </div>
      </div>
      <div class="dashboardContentContainer">
        <ContentCard timestamp="12:23:52 29.8. 2022" title="Test Announcement">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet est laoreet, sagittis lorem volutpat, molestie velit. Quisque at ligula a massa tristique rhoncus. Aliquam porta, dolor nec ullamcorper mollis, lacus enim congue mi, quis imperdiet dui orci a ex. Nunc aliquet mi sed tortor tincidunt, sed venenatis ipsum feugiat. Etiam nec rutrum urna, sit amet faucibus eros. Praesent odio tortor, consectetur ac suscipit sit amet, ultrices a lectus. Donec et convallis nisi. Vestibulum et posuere enim, at facilisis mauris. Etiam ut suscipit lorem. Etiam ut posuere tellus, ac auctor quam. Nullam urna magna, ultricies non nibh ac, commodo sodales lorem.

Maecenas a sem sem. Sed at semper orci. Nulla facilisi. Quisque tempus, nibh hendrerit porttitor rutrum, nulla ipsum malesuada mauris, vel finibus erat felis vel nibh. Fusce luctus tellus facilisis, bibendum lacus non, mollis quam. Quisque gravida ipsum ac magna congue tincidunt. Aenean auctor ut augue eget viverra. Aenean odio mi, sollicitudin id sodales non, vestibulum in enim. Phasellus turpis velit, fringilla at suscipit ac, sagittis molestie nisl. Aliquam consequat purus sapien, in eleifend metus pharetra ac. Ut sed egestas est. Mauris sodales mi quam, ac sagittis ex ultrices et.</ContentCard>
      </div>
    </div>
  </div>
</template>
<script>
import ContentCard from '@/components/ContentCard.vue';
import ButtonLink from '@/components/ButtonLink.vue';
import { getCurrentInstance } from 'vue';
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
      accountNumber: "",
      balance: 0,
      debts: [],
      remainingTotalDebt: 0, 
      monthlyTotalRepainmentPerFlat: 0
    }
  },
  components: {
    ContentCard,
    ButtonLink
  },

  methods: {
  },

  created: function(){
    if (!getCurrentInstance().parent.ctx.$parent.verified){
      this.$router.push("/login")
    }
  },

  mounted: function(){
    axios
      .get("http://127.0.0.1:5000/getAllDebts")
      .then((response) => {
        for (const [key, value] of Object.entries(response.data)){
            this.debts.push({
                totalDebt: value.total_debt,
                remainingDebt: value.remaining_debt,
                remainingDebtPerFlat: value.remaining_debt_per_flat,
                repaimentPerFlat: value.repainment_per_flat,
                debtId: key
            })

            this.remainingTotalDebt += value.total_debt;
            this.monthlyTotalRepainmentPerFlat += value.repainment_per_flat;
          }      
      });

    axios
      .get("http://127.0.0.1:5000/getFinancialsGeneral")
      .then((response) => {
        console.log(response.data)
          this.accountNumber = response.data.account_number.text;
          this.balance = response.data.account_balance.text;
      });
  }
}


</script>
<style scoped lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap');
@import "@/assets/colors.scss";

.dashboard {
  padding: 90px 0 0 0;
  min-height: 74vh;
  margin: 0;
  overflow-x: hidden;

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

            .dashboardFinancialQuickInfoTitle {
              font-weight: 700;
              font-size: 0.75rem;
              letter-spacing: 0.25em;
              color: $primary;
              margin: 0;
              text-align: left;
            }

            .dashboardFinancialQuickInfoText {
              font-weight: 700;
              font-size: 1.5rem;
              margin: 0;
              text-align: left;
            }
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

            .dashboardFinancialDocumentText {
              text-align: left;
              font-weight: 400;
              font-size: 1rem;
            }
          }

          .dashboardFinancialHeader {
            font-weight: 700;
            font-size: 2.5rem;
            text-align: left;
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
              margin: 0 10px 0 0;
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

                .dashboardFinancialPartHeader {
                  font-weight: 700;
                  font-size: 0.75rem;
                  letter-spacing: 0.25em;
                  color: $primary;
                  margin: 0;
                  text-align: left;
                }

                .dashboardFinancialContentText {
                  font-weight: 700;
                  font-size: 1.5rem;
                  margin: 5px 0 25px 0;
                  text-align: left;
                }
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