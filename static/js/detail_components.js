Vue.component('detail-item', {
  delimiters: ['[[', ']]'],
  props: [
    'detail_date',
    'detail_value',
    'detail_category',
    'detail_description',
  ],
  data: function(){
    return {
      state: 'hidden_accordion'
    }
  },
  methods: {
    view: function(){
      if (this.state == 'hidden_accordion'){
        this.state = 'visible_accordion';
      } else {
        this.state = 'hidden_accordion';
      }
    }
  },
  template: '#detail-item-template',
})
