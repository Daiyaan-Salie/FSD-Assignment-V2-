<template>
  <div class = "hello">
  <h1>Index Constituents and Weights of {{this.stock}}</h1>
    <!-- call the function -->
    <form @submit.prevent="updateStock">
    <input type="submit" value="Submit" class ="btn-primary">
    <input type ="text" v-model= "stock" name ="stock" placeholder="Select Ticker" >
  

    <div>




</div>

    </form >
       <!-- call the variable -->
    <div class="row" v-if="loaded">
       
    </div>
    

<div>




</div>



    <div class ='col-md-5'>
      <b-table :items="item" :fields="fields">
      </b-table>
    </div>





    
    <div class ='col-md-6'>
      <div id="Scatter"></div>


    

    <div class ='col-md-12'>
      <div id="myPie"></div>
    </div>
</div>
</div>
  
    </template>
    
    <script> 
    

import axios from 'axios'
import Plotly from 'plotly.js-dist';


    
    export default {
        name:'ConstituentsWeights',
        props: {
          msg: String
        },
        data(){

          // initialise all variables
            return{
                url: '',
                url2: '',
                url3: '',
                allfinancials:[],
                financials: [],
                stock: '',
                loaded: '',
                item:[],
                fields:[], 
                close: [],
                x:[],
                opentemp:'',
                xi: '',
                trace1:{},
                cash:[],
                inv: [],
                csti: [],
                rec: [],
                inv: [],
                currAsst: [],
            }
        },

        // divide number by R1m to make it more readable
        // methods contain the logic 
        
        methods: {

// create a pie chart


          getPie(stock){


            this.url3 = 'http://127.0.0.1:5000/api/synthetictable'
            console.log(this.url3) 
                axios.get(this.url3)
            .then (res => {


              this.cash = res.data[0]['cashAndCashEquivalents']
              this.inv= res.data[0]['shortTermInvestments']
              this.csti= res.data[0]['cashAndShortTermInvestments']
              this.rec= res.data[0]['netReceivables']
              this.inv = res.data[0]['inventory']
              this.currAsst = res.data[0]['otherCurrentAssets']

              console.log(this.cash)

            }
         
            )

            .catch (err => console.log(err))
            
            var data = [{
                values: [this.cash, this.inv,this.csti,this.rec,this.inv,this.currAsst],
                labels: ['cashAndCashEquivalents','shortTermInvestments', 'cashAndShortTermInvestments', 'netReceivables', 'inventory', 'otherCurrentAssets'],
                textinfo: "label+percent",
                textposition: "outside",
                title: "myPie",
                type: 'pie'
              }];

              var layout = {
                height: 400,
                width: 500
              };

              Plotly.newPlot('myPie', data, layout);


          },

            // Creating a scatter plot

          getChart(stock){
            this.url2 = 'https://financialmodelingprep.com/api/v3/historical-price-full/'+this.stock+'?timeseries=10&apikey=fc5921fae23cf964208ebb686edbc5a6' 
            console.log(this.url2) 
                axios.get(this.url2)
                .then( res => {
              this.close=[]
              this.x=[]  
              this.xi= ''
              this.opentemp = res.data.historical
              for (this.xi of this.opentemp){ 
               
                this.close.push(this.xi.close)
            
                this.x.push(this.xi.date)
              }
              console.log(this.close)
              console.log(this.x)

            })
            .catch(err => console.log(err))
            
            var trace1 = {
              x: this.x,
              y: this.close,
              mode: 'lines+markers',
              type: 'scatter',
              title: "Constituents",

            };

            var data=[trace1]

              Plotly.newPlot('Scatter',data);

              // end of scatter plot


},

          // format the figures in table             
            formatNumber(number){
                number = (number/1000000).toFixed(2).replace('.',',')
                return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g,".")

            },


            // Creating a table

            updateStock(){
                this.url = 'http://127.0.0.1:5000/api/synthetictable'
               
                console.log(this.url)
                axios.get(this.url)
                .then( res => {
                    this.allIndustries = res.data,
                    this.Industry = res.data[1];
                    this.loaded = true,
                    // define column labels
                    this.fields=['IS_Item', 'in_MillionsCY','in_MillionsPY']
                    // get variables from dictionary
                    this.item=[
                      { in_MillionsCY: "a",in_MillionsPY : "q", IS_Item: "a"},
                      {in_MillionsCY: this.allfinancials[0].date, in_MillionsPY : this.allfinancials[1].date, IS_Item: Object.keys(this.financials)[0]},
                      {in_MillionsCY: this.formatNumber(this.allfinancials[0].revenue), in_MillionsPY : this.formatNumber(this.allfinancials[1].revenue), IS_Item: Object.keys(this.financials)[8]},
                      {in_MillionsCY: this.formatNumber(this.allfinancials[0].costofRevenue), in_MillionsPY : this.formatNumber(this.allfinancials[1].costofRevenue), IS_Item: Object.keys(this.financials)[9]}
                    ]
                    this.getChart(this.stock)
                    this.getPie(this.stock)
                })
                .catch (err => console.log(err))
            
            }
        }
    
    }
    </script>
    
    <style>
    
    
    </style>