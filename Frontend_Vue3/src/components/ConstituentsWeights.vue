<template>
  <div class = "hello">
  <h1>Index Constituents and Weights of {{this.stock}}</h1>
    <!-- call the function -->
    <form @submit.prevent="updateStock">
    <input type="submit" value="Submit" class ="btn-primary">
    <input type ="text" v-model= "stock" name ="stock" placeholder="Select Year" >
  

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
      <div id="Weights per Industry"></div>
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
                url: 'http://127.0.0.1:5000/api/synthetictable',
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
                allIndustries: [],
                Beta: [],
                Industry1: [],
                Industry2: [],
                Industry3: [],
                Industry4: [],
                Industry5: [],
                Industry6: [],
                Industry7: [],
                Industry8: [],
                Industry9: [],
            }
        },

        // divide number by R1m to make it more readable
        // methods contain the logic 
        
        methods: {

// create a pie chart


          getPie(){


            // this.url3 = 'http://127.0.0.1:5000/api/synthetictable'
            console.log(this.url) 
                axios.get(this.url)
            .then (res => {


              this.Industry1 = res.data[0]['Weight']
              this.Industry2= res.data[1]['Weight']
              this.Industry3= res.data[2]['Weight']
              this.Industry4= res.data[3]['Weight']
              this.Industry5 = res.data[4]['Weight']
              this.Industry6 = res.data[5]['Weight']
              this.Industry7 = res.data[6]['Weight']
              this.Industry8 = res.data[7]['Weight']
              this.Industry9 = res.data[8]['Weight']


              console.log(this.cash)

            }
         
            )

            .catch (err => console.log(err))
            
            var data = [{
                values: [this.Industry1,this.Industry2,this.Industry3,this.Industry4,this.Industry5,this.Industry6,this.Industry7,this.Industry8,this.Industry9],
                labels: ['Oil & Gas','Basic Materials', 'Industrials', 'Consumer Goods', 'Health Care', 'Consumer Services','Telecommunications','Utilities','Financials','Technology'],
                textinfo: "label+percent",
                textposition: "outside",
                title: 'Weights per Industry',
                type: 'pie'
              }];

              var layout = {
                height: 400,
                width: 500
              };

              Plotly.newPlot('Weights per Industry', data, layout);


          },

            // Creating a scatter plot

          getChart(){
            // this.url2 = 'http://127.0.0.1:5000/api/synthetictable'
            console.log(this.url) 
                axios.get(this.url)
                .then( res => {
              this.Beta=[]
              this.x=[]  
              this.xi= ''
              this.opentemp = res.data
              for (this.xi of this.opentemp){ 
               
                this.Beta.push(this.xi.Beta)
            
                this.x.push(this.xi.date)
              }
              console.log(this.Beta)
              console.log(this.x)

            })
            .catch(err => console.log(err))
            
            var trace1 = {
              x: this.x,
              y: this.Beta,
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
                // this.url = 'http://127.0.0.1:5000/api/synthetictable'
               
                console.log(this.url)
                axios.get(this.url)
                .then( res => {
                    this.allIndustries = res.data,
                    // this.Industry = res.data[1];
                    this.loaded = true,
                    // define column labels
                    this.fields=['Date', 'Industry','Weight','Beta','SysVol','SpecVar']
                    // get variables from dictionary
                    this.item=[
                      // { Date: "a", Industry: "q", Weight: "a", Beta: "R", SysVol: "T", SpecVar: "G"},
                      { Date: this.allIndustries[0].Date, Industry: this.allIndustries[0].Industry, Weight: this.allIndustries[0].Weight, Beta: this.allIndustries[0].Beta[0][0], SysVol: this.allIndustries[0].SysVol, SpecVar: this.allIndustries[0].SpecVar},
                      { Date: this.allIndustries[1].Date, Industry: this.allIndustries[1].Industry, Weight: this.allIndustries[1].Weight, Beta: this.allIndustries[1].Beta[0][0], SysVol: this.allIndustries[1].SysVol, SpecVar: this.allIndustries[1].SpecVar},
                      { Date: this.allIndustries[2].Date, Industry: this.allIndustries[2].Industry, Weight: this.allIndustries[2].Weight, Beta: this.allIndustries[2].Beta[0][0], SysVol: this.allIndustries[2].SysVol, SpecVar: this.allIndustries[2].SpecVar},
                      { Date: this.allIndustries[3].Date, Industry: this.allIndustries[3].Industry, Weight: this.allIndustries[3].Weight, Beta: this.allIndustries[3].Beta[0][0], SysVol: this.allIndustries[3].SysVol, SpecVar: this.allIndustries[3].SpecVar},
                      { Date: this.allIndustries[4].Date, Industry: this.allIndustries[4].Industry, Weight: this.allIndustries[4].Weight, Beta: this.allIndustries[4].Beta[0][0], SysVol: this.allIndustries[4].SysVol, SpecVar: this.allIndustries[4].SpecVar},
                      { Date: this.allIndustries[5].Date, Industry: this.allIndustries[5].Industry, Weight: this.allIndustries[5].Weight, Beta: this.allIndustries[5].Beta[0][0], SysVol: this.allIndustries[5].SysVol, SpecVar: this.allIndustries[5].SpecVar},
                      { Date: this.allIndustries[6].Date, Industry: this.allIndustries[6].Industry, Weight: this.allIndustries[6].Weight, Beta: this.allIndustries[6].Beta[0][0], SysVol: this.allIndustries[6].SysVol, SpecVar: this.allIndustries[6].SpecVar},
                      { Date: this.allIndustries[7].Date, Industry: this.allIndustries[7].Industry, Weight: this.allIndustries[7].Weight, Beta: this.allIndustries[7].Beta[0][0], SysVol: this.allIndustries[7].SysVol, SpecVar: this.allIndustries[7].SpecVar},
                      { Date: this.allIndustries[8].Date, Industry: this.allIndustries[8].Industry, Weight: this.allIndustries[8].Weight, Beta: this.allIndustries[8].Beta[0][0], SysVol: this.allIndustries[8].SysVol, SpecVar: this.allIndustries[8].SpecVar},
                      { Date: this.allIndustries[9].Date, Industry: this.allIndustries[9].Industry, Weight: this.allIndustries[9].Weight, Beta: this.allIndustries[9].Beta[0][0], SysVol: this.allIndustries[9].SysVol, SpecVar: this.allIndustries[9].SpecVar}

                    ]
                    this.getChart()
                    this.getPie()
                })
                .catch (err => console.log(err))
            
            }
        }
    
    }
    </script>
    
    <style>
    
    
    </style>