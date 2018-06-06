Vue.component('detail-item', {
  delimiters: ['[[', ']]'],
  props: [
  	'detail_id',
    'detail_date',
    'detail_value',
    'detail_category',
    'detail_description',
  ],
  data: function(){
    return {
      state: 'hidden_accordion',
      widget_info: '',
      modal_state: 'hidden_accordion',
    }
  },
  methods: {
    view: function(){
      if (this.state == 'hidden_accordion'){
        this.state = 'visible_accordion';
      } else {
        this.state = 'hidden_accordion';
      }
    },
    ask_modal: function(){
    	this.$emit('display_modal', this);
    }
  },
  template: `
  <div class="tx_upper_line">
  <div class="pure-u-1-3 tx_date">
    [[ detail_date ]]
  </div>
  <div class="pure-u-1-3 tx_value">
    $ [[ detail_value ]]
  </div>
  <div class="pure-u-1-3 tx_category">
    <button v-on:click="view" type="button" name="button">[[ detail_category ]] (...)</button>
  </div>
  <div class="pure-u-1" v-bind:class="state">
    [[ detail_description ]]
    <button class="tx_category" v-on:click="ask_modal" type="button">(edit)</button>
  </div>

</div>
  `
})
