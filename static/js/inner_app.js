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
created: function(){
    this.consume_api();
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
  consume_api: function(){
    var url = '../workout/exercises/json/';
    fetch(url).then(
      function response(response){
        return response.json();
      }
    ).then(
      function (data) {
        var new_data = [];
        for (i in data['data']){
          var item = data['data'][i];
          new_data.push(item);
        }
        app.exercisesList = new_data;
      }
    )
  }
}
})
