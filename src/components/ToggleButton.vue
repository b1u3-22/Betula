<template>
    <div @click="handleChange" class="toggleContainer" :class="{toggleContainerChecked: checked, toggleContainerUnchecked: !checked}">
        <div class="toggleCircle" />
    </div>
</template>

<script>
export default {
  name: 'ToggleButton',
  components: {

  },
  props: {
    isChecked: {
        type: Boolean,
        default: false
    }
  },

  methods: {
    handleChange: function(){
        this.checked = !this.checked
        this.$emit("update:checked", this.checked)
        this.$emit("change")
    }
  },

  data: function() {
      return {
        checked: this.isChecked
      }
  }
}
</script>

<style scoped lang="scss">

@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap');
@import "@/assets/colors.scss";

.toggleContainer {
    display: flex;
    flex-flow: column nowrap;
    align-items: flex-start;
    justify-content: center;
    border-radius: 1.25rem;
    height: 2.5rem;
    width: 5.4rem;
    transition: all 120ms ease-in-out;
    margin: 10px;

    .toggleCircle {
        background-color: $text-dark;
        width: 1.6rem;
        height: 1.6rem;
        border-radius: 50%;
        margin: 0 0.4rem;
        transition: all 120ms ease-in-out;
    }
}

.toggleContainerUnchecked {
    background-color: $shadows-light;
}

.toggleContainerChecked {
    background-color: $primary;

    .toggleCircle {
        margin: 0 0.4rem 0 3.4rem;
    }
}

</style>
