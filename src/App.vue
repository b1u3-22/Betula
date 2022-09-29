<template>
  <nav>
    <router-link to="/" class="nav-item">
      Domů
      <div class="nav-line" />
    </router-link>
    <router-link to="/home-gallery" class="nav-item">
      Galerie
      <div class="nav-line" />
    </router-link>
    <router-link to="/home-contact" class="nav-item">
      Kontakt
      <div class="nav-line" />
    </router-link> 
    <router-link to="/login" class="nav-item">
      Přihlášení
      <div class="nav-line" />
    </router-link>
  </nav>
  <router-view />
  <footer>
    <div class="footerTextContainer">
      <div class="footerMenuContainer">
        <h4 class="footerTitle">Menu</h4>
        <a class="footerItem">Domů</a>
        <a class="footerItem">Galerie</a>
        <a class="footerItem">Kontakty</a>
        <a class="footerItem">Přihlášení</a>
      </div>
      <div class="footerMenuContainer">
        <h4 class="footerTitle">Kontakt</h4>
        <p class="footerItem">Lorem Ipsum</p>
        <p class="footerItem">Lorem Ipsum</p>
        <p class="footerItem">Lorem Ipsum</p>
        <p class="footerItem">Lorem Ipsum</p>
      </div>
    </div>
    <div class="footerCopyright">© Jiří Sedlák 2022</div>
  </footer>
</template>

<style lang="scss">

@import "@/assets/colors.scss";
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap');

html {
  overflow-x: hidden !important;
  -webkit-overflow-scrolling: touch;
  font-size: 16px;
}

body {
  margin: 0;
  padding: 0;
}

#app {
  font-family: 'Montserrat', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: black;
  background-color: $background-light;
}

nav {
  padding: 15px;
  position: fixed;
  top: 0;
  width: 100vw;
  display: flex;
  flex-flow: row nowrap;
  justify-content: center;
  align-items: flex-start;
  background-color: $background-dark;
  box-shadow: 0px 10px 15px rgba(0, 0, 0, 0.25);
  z-index: 999999;

  .router-link-exact-active {
    .nav-line {
      width: 100% !important;
    }
  }

  .nav-item {
  font-weight: 600;
  font-size: 1.125rem;
  display: flex;
  flex-flow: column nowrap;
  align-items: flex-end;
  justify-content: flex-start;
  width: fit-content;
  text-decoration: none;
  color: $background-light;
  margin: 0 2%;

    .nav-line {
      display: inline;
      width: 0%;
      height: 3px;
      background-color: $primary;
      transition: all 200ms ease-in-out;
    }

    &:hover {
      align-items: flex-start;
    }

    &:hover > .nav-line{
      width: 100%;

    }

    .router-link-exact-active {
      color: $primary
    }

  }
}

footer {
  background-color: #F1F1F1;
  display: flex;
  flex-flow: column nowrap;
  justify-content: flex-end;
  align-items: stretch;
  padding: 2% 3% 1% 3%;

  .footerTextContainer {
    display: flex;
    flex-flow: row nowrap;
    align-items: flex-start;
    justify-content: flex-start;

    .footerMenuContainer {
      display: flex;
      flex-flow: column nowrap;
      justify-content: flex-start;
      align-items: flex-start;
      margin: 0 10% 0 0;

      .footerTitle {
        margin: 0;
        padding: 0;
        font-size: 1.125rem;
        font-weight: 700;
      }

      .footerItem {
        margin: 3px 0;
        padding: 0;
        font-size: 1rem;
        font-weight: 400;
        cursor: pointer;
      }
    }
  }
}

@media (max-width: 1000px) {
  html {
    font-size: 12px;
  }
}

@media (max-width: 700px) {
  html {
    font-size: 8px;
  }
}

@media (max-width: 600px) {
  html {
    font-size: 14px;
  }

  footer {
    padding: 4% 6% 2% 6%;

    .footerTextContainer {
      margin-bottom: 22px;
    }
  }
}


</style>
