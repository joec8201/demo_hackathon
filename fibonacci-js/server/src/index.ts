import { ethers } from "ethers";
import { startServer, BaseApplication, StepEvent } from '@sparsity/abci';


// customized app logic
export class Application extends BaseApplication {
    private result: number;

    constructor() {
        super();
        this.result = 0;
    }
    
    init(initial_data: string) {
        // the initial_data is the data from contract
        if (initial_data != "") {
            const decoded = ethers.AbiCoder.defaultAbiCoder().decode(['uint256'], initial_data);
            const n = Number(decoded[0])
            this.result = this.inverseTransform(n);
            console.log("Computing mean of " + n + " random standard normal samples ON THE BLOCKCHAIN:")
            console.log("Gaussian Mean result", this.result);
            console.log("Gaussian Mean encoded result", this.encodeFloatAsHex(this.result))
        } else {
            // it can be empty string if no initial data sent by contract
            this.result = 1;
            console.log("no inital data")
        }
    }

    step(messages: Array<any>): Array<StepEvent> {
        var events: Array<StepEvent> = [];
        return events;
    }

    status(): [isEnd: boolean, data: string] {
        // set isEnd to true if CORE finished calculating the number
        if (this.result == 0) {
            return [false, ""];
        }
        // the data should be encoded with abi
        return [true, this.resultData()];
    }

    inverseNormalCDF(p: number): number {
         return -Math.log((1 / p) - 1) / 1.702
    }

    inverseTransform(n: number) {
        let res = new Array(n).fill(0)
        for(let i = 0; i < n; i++){
            res[i] = this.inverseNormalCDF(Math.random())
            }
        const sum = res.reduce((a, b) => a + b, 0);
        return sum / n
    }

    encodeFloatAsHex(x: number){
        return Math.round(x * Math.pow(10, 10)).toString(16)
    }

    resultData() {
        return ethers.AbiCoder.defaultAbiCoder().encode(["int256"], [this.result]);
    }
}

startServer(new Application());
