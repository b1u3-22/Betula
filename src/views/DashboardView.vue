<template>
  <div class="dashboard">
    <div class="dashboardMainContainer">
      <div class="dashboardFinancialContainer">
        <div class="dashboardFinancialHeaderContainer">
          <div class="dashboardFinancialButtonsContainer">
            <img :src="require(`@/assets/icons/circleArrowIcon.svg`)" class="dashboardFinancialRollButton" :class="{dashboardFinancialButtonRollUp: financialRolledUp, dashboardFinancialButtonRollDown: !financialRolledUp}" @click="financialRolledUp = !financialRolledUp" />
          </div>
          <div :class="{dashboardFinanctialQuickInfoShowed: financialRolledUp, dashboardFinanctialQuickInfoHidden: !financialRolledUp}" class="dashboardFinancialQuickInfo">
            <div class="dashboardFinancialQuickInfoContentContainer">
              <div class="dashboardFinancialQuickInfoTitle">Zůstatek na účtu</div>
              <div class="dashboardFinancialQuickInfoText">1 256 264 Kč</div>
            </div>
            <div v-if="remainingTotalDebt !== 0" class="dashboardFinancialQuickInfoContentContainer">
              <div class="dashboardFinancialQuickInfoTitle">Zbývající dluh</div>
              <div class="dashboardFinancialQuickInfoText"> {{ remainingTotalDebt }} </div>
            </div>
            <div v-if="monthlyTotalRepainmentPerFlat !== 0" class="dashboardFinancialQuickInfoContentContainer">
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
                      <p class="dashboardFinancialContentText">{{ debt.wholeDebt }}</p>
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
                      <p class="dashboardFinancialContentText">{{ debt.monthlyRepainmentPerFlat }}</p>
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


export default {
  name: 'DashboardView',
  data: function() {
    return {
      financialRolledUp: true,
      accountNumber: "2698 6426 6642 / 0880",
      balance: 1254850,
      debts: [],
      remainingTotalDebt: 0, 
      monthlyTotalRepainmentPerFlat: 0
    }
  },
  components: {
    ContentCard
},
  methods: {
  },
  mounted: function(){
    this.debts = [{wholeDebt: 2000000, remainingDebt: 300500, remainingDebtPerFlat: 60000, monthlyRepainmentPerFlat: 500}, {wholeDebt: 3000000, remainingDebt: 600500, remainingDebtPerFlat: 90000, monthlyRepainmentPerFlat: 1500}];
    
    for(let debt of this.debts){
      this.remainingTotalDebt += debt.remainingDebt;
      this.monthlyTotalRepainmentPerFlat += debt.monthlyRepainmentPerFlat;
    }
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
        align-items: flex-start;
        width: 100%;

        .dashboardFinancialButtonsContainer {
          display: flex;
          flex-flow: row nowrap;
          justify-content: flex-end;
          align-items: center;

          .dashboardFinancialRollButton {
            cursor: pointer;
            transition: all 220ms ease-in-out;
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
          margin-top: -50px;
          //animation: dashboardFinancialRollAnimation 500ms ease-in-out reverse;

          .dashboardFinancialSubContainer {
          display: flex;
          flex-flow: column nowrap;
          justify-content: flex-start;
          align-items: flex-start;
          margin: 0 7% 0 0;

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
            margin: 0 20% 0 0;
            min-width: 50%;

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
                  margin: 10px 0 25px 0;
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

.dashboardFinancialRollUp {
  max-height: 0vh;
  opacity: 0;
}

.dashboardFinancialRollDown {
  opacity: 1;
  max-height: 100vh;
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

</style>