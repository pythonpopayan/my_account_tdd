var app = new Vue({
el: '#app',
delimiters: ['[[', ']]'],
data: {
  panel_state: '',
  exercisesList: [],
  widget_info: '',
  modal_state: 'visible_accordion',
  form_state: {},
  form_action_url: '',
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
  show_modal: function(item_obj){
  	this.form_action_url = '../../../account/edit-transaction/'+item_obj.detail_id;
  	this.form_state = item_obj;
    var w = document.getElementById('die_glucke');
    w.style.display='block';
  },
  close_modal: function(){
  	var w = document.getElementById('die_glucke');
    w.style.display='none';
  },
  edit_register: function(){
    // get elements
    // build request body
    // send request
    
  }
}
})
