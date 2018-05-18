Vue.component('exercises-item', {
  props: ['exercise'],
  delimiters: ['[[', ']]'],
  template: '#exercises-template'
})

var app = new Vue({
el: '#app',
delimiters: ['[[', ']]'],
data: {
  panel_state: '',
  exercisesList: [],
},
methods: {
  tooglePanel: function() {
    // shows and hides panel on small screens
    if (this.panel_state === '') {
      this.panel_state = 'active'
    }
    else {
      this.panel_state = ''
    }
  },
  tx_accordion: function() {
      // get id of description picked
      // toogle description picked
  },
}
})
