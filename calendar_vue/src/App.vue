<template>
  <div>
    <header class="app-header">
      <h2><router-link class="app-button-tp" style="text-decoration: none;"
        to=/about>Skdue</router-link></h2>
      <EventCreate />
    </header>
    <body class="app-body">
      <router-view/>
    </body>
  </div>
</template>

<script>
import EventCreate from './components/EventCreate'
export default {
  components: {
    EventCreate
  }
}
</script>

<style lang="scss">

@import './assets/style.css';
@import './assets/color.css';

.app-header {
  background: var(--main-green);
  color: var(--main-green);
  font-size: 25px;
  font-weight: 500px;
  line-height: 0px;
  height: 65px;
  display: flex;
  justify-content: space-around;  
  z-index: 5;
  position: fixed !important;
  top: 0px;
  left: 0px;
  right: 0px;
}

.app-body {
  position: absolute;
  top: 20px;
  right: 0px;
  left: 0px;
}

</style>