<template>
  <div>
    <header>
      <div id="nav">
        <h2><router-link style="text-decoration: none; color: inherit; font-size: 40px;"
          to="/about">Skdue</router-link></h2>
      </div>
      <EventCreate />
    </header>
    <router-view/>
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
* {
  font-family: Calibri, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

header {
  background: rgb(0, 102, 100);
  color: white;
  font-weight: 500;
  line-height: 75px;
  padding: 0px 0px 0px 30px;
  height: 80px;
  display: flex;
  justify-content: space-between;  
  z-index:5;
  position:relative;
}
#nav {
  line-height: 75px;
}

</style>