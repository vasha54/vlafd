/*Clases*/
Point=(function(){
	
    function Point(){
	 	this.x=0;
		this.y=0;
        this.label='';
	};
	
    Point.prototype.getX=function(){ return this.x; };
    Point.prototype.setX=function(_x){ this.x=_x;};
    Point.prototype.getY=function(){ return this.y;};
    Point.prototype.setY=function(_y){ this.y=_y; };
    Point.prototype.setLabel=function(_label){ this.label=_label; };
    Point.prototype.getLabel=function(){ return this.label; };
    Point.prototype.print=function(){ console.log("x:"+this.x+ " y:"+this.y)};
    return Point;
})();

Circle=(function(){
	
    function Circle(){
	 	this.x=0;
		this.y=0;
		this.radius=0;
	};

    Circle.prototype.getX=function(){ return this.x; };
    Circle.prototype.setX=function(_x){ this.x=_x; };
    Circle.prototype.getY=function(){ return this.y; };
    Circle.prototype.setY=function(_y){ this.y=_y; };
    Circle.prototype.getRadius=function(){ return this.radius; };
    Circle.prototype.setRadius=function(_radius){ this.radius=_radius; };
    Circle.prototype.print=function(){ console.log("x:"+this.x+ " y:"+this.y+" radius:"+this.radius)};
    return Circle;
})();

RectMxplusN=(function(){
	
    function RectMxplusN(){
	 	this.m=0;
		this.n=0;
        this.X1=0;
        this.Y1=0;
        this.X2=0;
        this.Y2=0;
        this.parallelX=false;
        this.parallelY=false;
	};

    RectMxplusN.prototype.getM=function(){ return this.m; };
    RectMxplusN.prototype.setM=function(_m){ this.m=_m; };
    RectMxplusN.prototype.getN=function(){ return this.n; };
    RectMxplusN.prototype.setN=function(_n){ this.n=_n; };
    RectMxplusN.prototype.print=function(){ console.log("m:"+this.m+ " n:"+this.n)};
    RectMxplusN.prototype.isParallelX=function (){ return this.parallelX};
    RectMxplusN.prototype.isParallelY=function (){ return this.parallelY};
    RectMxplusN.prototype.getPointBegin=function (){ return this.pointBegin};
    RectMxplusN.prototype.getPointEnd=function (){ return this.pointEnd};
    RectMxplusN.prototype.getX1=function(){return this.X1};
    RectMxplusN.prototype.getY1=function(){return this.Y1};
    RectMxplusN.prototype.getX2=function(){return this.X2};
    RectMxplusN.prototype.getY2=function(){return this.Y2};
    RectMxplusN.prototype.setPointBegin=function (_x1 ,_y1){
        this.X1=_x1;
        this.Y1=_y1;
        
        if(this.X1==this.X2)
            this.parallelY=true;
        
        if(this.Y1==this.Y2)
            this.parallelX=true;
        
        if(this.parallelX==false && this.parallelY==false)
        {
            this.m=(this.Y1-this.Y2)/(this.X1-this.X2);
            this.n=this.Y1-(this.m*this.X1);
        }
        else
        {
            this.m=0;
            this.n=0;
        }
    };
    
    RectMxplusN.prototype.setPointEnd=function (_x2 ,_y2){
        this.X2=_x2;
        this.Y2=_y2;
        
        if(this.X1==this.X2)
            this.parallelY=true;
        
        if(this.Y1==this.Y2)
            this.parallelX=true;
        
        if(this.parallelX==false && this.parallelY==false)
        {
            this.m=(this.Y1-this.Y2)/(this.X1-this.X2);
            this.n=this.Y1-(this.m*this.X1);
        }
        else
        {
            this.m=0;
            this.n=0;
        }
    };
    
     RectMxplusN.prototype.evaluateX=function (_x)
     {
       return (this.m*_x)+this.n;  
     };
    return RectMxplusN;
})();

