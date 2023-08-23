from flask import Flask, request, render_template, url_for
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Generate URLs for the other Flask pages
    print("Generating URL for page1")
    page1_url1 = url_for('index1')
    page1_url2 = url_for('dlt')
    # Pass the URLs to the main Flask view
    return render_template("home1.html", page1_url1=page1_url1, page1_url2=page1_url2)

@app.route('/dlt1', methods=['GET', 'POST'])
def dlt():
    # Generate URLs for the other Flask pages
    print("Generating URL for page1")
    page1_url2 = url_for('page3')
    # Pass the URLs to the main Flask view
    return render_template("home2.html", page1_url2=page1_url2)

@app.route('/index', methods=['GET', 'POST'])
def index1():
    # Generate URLs for the other Flask pages
    print("Generating URL for page1")
    page1_url = url_for('page1')
    page2_url = url_for('page2')
    page3_url = url_for('page3')
    page4_url = url_for('page4')

    # Pass the URLs to the main Flask view
    return render_template("home.html", page1_url=page1_url, page2_url=page2_url,page3_url=page3_url,page4_url=page4_url)

@app.route('/contourbund', methods=['GET', 'POST'])
def page1():
    if request.method == 'POST':
        s = float(request.form['s'])
        vi = round((10 * s + 60) / 100, 2)
        hi = round(vi / s * 100, 2)
        r = float(request.form['r'])
        z = float(request.form['z'])
        d = round(math.sqrt((2 * (r * hi * vi) / (hi + ( z * vi)))), 2)
        w= round(((hi * d )/ vi) + z*d, 2)
        fb = float(request.form['fb'])
        h = round((1 + fb / 100) * d, 2)
        zs = float(request.form['zs'])
        B = round((z*d) + (zs*d), 2)
        T = round((B - (2 * z * h)), 2)
        a = round(((T + B) / 2 ) * h,2)
        lbh= round((10000/hi), 2)
        vew = round((lbh * a), 2)  
        add20 = round((1.2 * vew), 2)
        cost = float(request.form['cost'])
        cbph= round(cost * add20, 2)
        img_src = "static\\svg.jpg?s={}&vi={}&hi={}&r={}&w={}&z={}&d={}&fb={}&h={}&zs={}&B={}&T={}&a={}&lbh={}&vew={}&add20={}&cost={}&cpbh={}".format(s, vi, hi, r, w, z, d, fb, h, zs, B, T, a, lbh, vew, add20, cost, cbph)
        return render_template('sc_result.html', s=s, vi=vi, hi=hi, r=r, w=w, z=z, d=d, fb=fb, h=h, zs=zs, B=B, T=T, a=a, lbh=lbh, vew=vew, add20=add20, cost=cost, cbph=cbph, img_src=img_src)
    else:
        return render_template('sc_index.html')

    

@app.route('/contourstonebund', methods=['GET', 'POST'])
def page2():
    if request.method == 'POST':
        s = float(request.form['s'])
        r = float(request.form['r'])
        
        if r>=1500:
            vi=round((s/10) + 1.5, 2)
        else:
            vi = round((s/10) + 2, 2)
        hi = round(vi / s * 100, 2)
        TL = round(100*s/vi, 2)
        h = float(request.form['h'])
        h1 = float(request.form['h1'])
        thob = round(h+h1, 2)
        b = round(2*h/3, 2)
        if b<=0.8:
            b=0.8
        Bt = float(request.form['Bt'])
        Af = round(b*h1, 2) 
        As = round((Bt + b)/2*h, 2)
        vocsb = round((Af+As)*TL, 2)
        ewif = round((TL*b)*h, 2)
        Ec = round((ewif*250), 2)
        sbc = round((vocsb*500), 2)
        tec = round((Ec+sbc), 2)


        
        img_src = "static\\csbsvg.jpg?s={}&r={}&vi={}&hi={}&TL={}&h={}&h1={}&thob={}&b={}&Bt={}&Af={}&As={}&vocsb={}&ewif={}&Ec={}&sbc={}&tec={}".format(s, r, vi,  hi, TL, h, h1, thob, b, Bt, Af, As, vocsb, ewif, Ec, sbc,tec )
        return render_template('csb_result.html', s=s, r=r, vi=vi, hi=hi, TL=TL, h=h, h1=h1, thob=thob, b=b, Bt=Bt,  Af=Af, As=As, vocsb=vocsb, ewif=ewif, Ec=Ec, sbc=sbc, tec=tec, img_src=img_src)
    else:
        return render_template('csb_index.html')
    
    
@app.route('/LBCD', methods=['GET', 'POST'])
def page3():
      if request.method == 'POST':
        wos = float(request.form['wos'])
        dos = float(request.form['dos'])
        nos = float(request.form['nos'])
        tw = 0.6
        hos = round((0.66*dos), 2)
        z1 = 1.5
        z2 = 2
        bwoss = round(tw+(hos*z1)+(hos*z2), 2)
        usal = 0.45
        dsal = 0.6
        tbw = round((bwoss + usal + dsal), 2)
        dof = 0.3
        vof = round((dof*tbw*wos), 2)
        doc = 0.6
        voc = round((wos*doc*usal)+((wos+0.9)*tw*doc)+(wos+0.9)*doc*dsal, 2)
        voss = round((((tw+bwoss)/2)*hos)*wos, 2)
        dssl = round(math.sqrt(hos**2+(z2*hos)**2), 2)
        vow = round((dssl*dsal*tw*2), 2)
        tvots = round((voc+voss+vof+vow), 2)
        
        img_src = "static\\svg.png?wos={}&dos={}&nos={}&tw={}&hos={}&z1={}&z2={}&bwoss={}&usal={}&dsal={}&tbw={}&dof={}&vof={}&doc={}&voc={}&voss={}&dssl={}&vow={}&tvots={}".format(wos, dos,  nos, tw, hos, z1, z2, bwoss, usal, dsal, tbw, dof, vof, doc, voc, voss, dssl, vow, tvots)
        return render_template('lbcd_result.html',wos=wos, dos=dos, nos=nos, tw=tw, hos=hos, z1=z1, z2=z2, bwoss=bwoss, usal=usal, dsal=dsal, tbw=tbw, dof=dof, vof=vof,doc=doc, voc=voc, voss=voss, dssl=dssl, vow=vow, tvots=tvots,img_src=img_src)
      else:
        return render_template('lbcd_index.html')
      

@app.route('/trenchbund', methods=['GET', 'POST'])
def page4():
    if request.method == 'POST':
        p = float(request.form['p'])
        v = float(request.form['v'])
        si = float(request.form['si'])
        Dsoil =float(request.form['Dsoil'])
        Wplot = float(request.form['Wplot'])
        Lplot = float(request.form['Lplot'])
        PP = float(request.form['PP'])
        RR= float(request.form['RR'])
        cn2 = float(request.form['cn2'])
        W = float(request.form['W'])
        D = float(request.form['D'])
        X = float(request.form['X'])
        L = float(request.form['L'])
        cn3 = cn2*math.exp(0.00673*(100-cn2))
        λ = 0.3
        s = round(25400/cn3-254, 2) 
        Ia = λ*s
        Q = round(math.pow((p-Ia), 2)/(p-Ia + s), 1)/10
        A = W * D
        HiST = A/(v*Q*(1 + X/L))
        HiCCT = A/(v*Q)
        ViST = si * HiST/100
        ViCCT = si * HiCCT/100
        LtotalST = (v/100)*(Q/100 * math.pow(10,4))/(A * math.pow(10,-4))
        LtotalCCT = (v/100)*(Q/100 * math.pow(10,4))/(A * math.pow(10,-4))
        NoTSTha = LtotalST/L
        NoTCCTha = LtotalCCT/Lplot
        Vearth = (v/100) * Lplot * Wplot * Q/100
        RoEW = float(request.form['RoEW'])
        CPA = Vearth * RoEW

        
        img_src = "static\\svg.png?p={}&v={}&si={}&Dsoil={}&Wplot={}&Lplot={}&PP={}&RR={}&cn2={}&cn3={}&λ={}&s={}&Ia={}&Q ={}&W={}&D={}&A={}&X ={}&L={}&HiST={}&HiCCT={}&ViST={}&ViCCT={}&LtotalST={}&LtotalCCT={}&NoTSTha={}&NoTCCTha={}&Vearth={}&RoEW={}&CPA={}".format(p, v, si,Dsoil,Wplot,Lplot,PP,RR,cn2,cn3,λ,s,Ia,Q,W,D,A,X,L,HiST,HiCCT,ViST,ViCCT,LtotalST,LtotalCCT,NoTSTha,NoTCCTha,Vearth,RoEW,CPA)
        return render_template('trench_result.html', p=p, v=v, si=si,Dsoil=Dsoil,Wplot=Wplot,Lplot=Lplot,PP=PP,RR=RR,cn2=cn2,cn3=cn3,λ=λ,s=s,Ia=Ia,Q=Q,W=W,D=D,A=A,X=X,L=L,HiST=HiST,HiCCT=HiCCT,ViST=ViST,ViCCT=ViCCT,LtotalST=LtotalST,LtotalCCT=LtotalCCT,NoTSTha=NoTSTha,NoTCCTha=NoTCCTha,Vearth=Vearth,RoEW=RoEW,CPA=CPA)
    else:
        return render_template('trench_index.html')



 
if __name__ == '__main__':
    app.run(debug=True)


