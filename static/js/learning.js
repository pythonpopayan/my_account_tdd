Vue.component('animal-item', {
  props: ['animal'],
  template: '<p><b> {{ animal.name }}:</b> {{ animal.description }}</p>'
})

var app = new Vue({
el: '#app',
delimiters: ['[[', ']]'],
data: {
  panel_state: 'meow',
  elementList: [],
},
created: function(){
  console.log('hi there buddy!!');
  this.fetchItems();
},
methods: {
  fetchItems (){
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
        app.elementList = new_data;
        console.log(app.elementList);
      }
    )
  }
}
})
