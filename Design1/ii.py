from flask import Flask, request, render_template, url_for
import math
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Generate URLs for the other Flask pages
    print("Generating URL for page1")
    page1_url1 = url_for('index1')
    page1_url2 = url_for('dlt')
    # Pass the URLs to the main Flask view
    return render_template("frontbanner.html", page1_url1=page1_url1, page1_url2=page1_url2)

@app.route('/dlt1', methods=['GET', 'POST'])
def dlt():
    # Generate URLs for the other Flask pages
    print("Generating URL for page1")
    page1_url3 = url_for('index2')
    # Pass the URLs to the main Flask view
    return render_template("dlt.html", page1_url3=page1_url3)
@app.route('/index', methods=['GET', 'POST'])
def index1():
    # Generate URLs for the other Flask pages
    print("Generating URL for page1")
    page2_url = url_for('page')
    page1_url = url_for('page1')
    page4_url = url_for('page2')
    page6_url = url_for('page3')
    page5_url = url_for('page4')
    page7_url = url_for('page5')

    # Pass the URLs to the main Flask view
    return render_template("soilstructure.html", page1_url=page1_url,page2_url=page2_url,page4_url=page4_url,page6_url=page6_url,page5_url=page5_url,page7_url=page7_url)

@app.route('/dl', methods=['GET', 'POST'])
def index2():
    total_length = 0
    output = ""
    form  = ""; form1  = ""; form2= ""
    highest_elevation = 0
    lowest_elevation = 0
    stream_order = 0
    bcdlength = 0
    wos = 0
    dos = 0
    lbcdlength = 0
    bcdlength1 = 0
    highest_elevation2 = 0
    lowest_elevation2 = 0
    bcd1_output1 = ""
    

    if request.method == 'POST':
        if 'total_length' in request.form and  request.form['total_length'].strip():
            total_length = float(request.form['total_length'])
        
            stream_order = request.form.get('stream_order', '')
            if stream_order == '1st':
                if total_length <= 200:
                    output = 'bcd'
                    bcdlength = total_length
                else:
                    output = 'bcd, lbcd'
                    bcdlength = 200
                    lbcdlength = round(total_length - bcdlength, 2)
            elif stream_order == '2nd':
                if total_length <= 200:
                    output = 'lbcd'
                    lbcdlength = total_length
                else:
                    output = 'lbcd, gs'
                    lbcdlength = 200
                    bcdlength1 = round(total_length - lbcdlength, 2)

            if output == "bcd":
                form1 = "visible"

            elif output=="lbcd":
                form  = "visible1"
            if output == 'bcd, lbcd':
                form1 = "visible"
                form  = "visible1"
            else:
                if output == "lbcd, gs": 
                    form  = "visible1"
                    form2  = "visible3"


    return render_template('DLT_index.html', total_length=total_length, stream_order=stream_order,
                           output=output, form = form ,form1=form1,form2=form2,
                           highest_elevation=highest_elevation, lowest_elevation=lowest_elevation,
                           bcdlength=bcdlength, lbcdlength=lbcdlength, wos=wos, dos=dos,
                           highest_elevation1=0, lowest_elevation1=0, bcdlength1=bcdlength1,
                           highest_elevation2=highest_elevation2, lowest_elevation2=lowest_elevation2,
                           bcd1_output1=bcd1_output1)


@app.route('/bcd', methods=['POST'])
def bcd():
    nos = 0; slope= 0; lnsebcd= 0; selbcd=0; hibcd=0; 
    intervl = None
    To_cost_con = None
    if 'highest_elevation' in request.form and  request.form['highest_elevation'].strip():
        highest_elevation = float(request.form['highest_elevation'])
    else:
            highest_elevation = 0
   
    if 'lowest_elevation' in request.form and  request.form['lowest_elevation'].strip():
         lowest_elevation = float(request.form['lowest_elevation'])
      
    else:
            lowest_elevation = 0

    bcdlength = float(request.form.get('bcdlength', 0))
    wos_input = request.form.get('wos',0)
    wos = float(wos_input) if wos_input.strip() else 0
    dos_input = request.form.get('dos',0)
    dos = float(dos_input) if dos_input.strip() else 0
    ed = highest_elevation - lowest_elevation
    if bcdlength*bcdlength-ed*ed>=0:
        hibcd = round(math.sqrt((bcdlength * bcdlength) - (ed * ed)), 2)
   
        slope = round((ed / hibcd) * 100, 2)
        lnsebcd = round(((-2.27) + (1.38 * (np.log(slope))) - (0.56 * np.log(dos)) + (0.25 * np.log(wos))), 2)
        selbcd = round(math.exp(lnsebcd), 2)
        nos = round((slope - selbcd) / dos)

  
    if nos == 1:
        intervl = hibcd
    else:
        intervl = round(hibcd / (nos - 1))
    cost_per_length = 500
    unit_cost = cost_per_length * wos
    To_cost_con = unit_cost * nos

    return render_template('DLT_index.html', highest_elevation=highest_elevation, lowest_elevation=lowest_elevation,
                           wos=wos, dos=dos, cost_per_length=cost_per_length, ed=ed, lnsebcd=lnsebcd,
                           sebcd=selbcd, nos=nos, intervl=intervl, slope=slope, hibcd=hibcd,
                           unit_cost=unit_cost, To_cost_con=To_cost_con, bcdlength=bcdlength)


@app.route('/lbcd', methods=['POST'])
def lbcd():
    hilbcd = slope = lnselbcd = selbcd = nos = intervl = bwoss = usal = dsal = tbw = dof = vof = doc = voc = voss = dssl = vow = tvots = sur_and_demar = cost_for_dig_found = cost_ston_pack = cost_for_stp_sup = sub_to_cost = cntgency_of_st = total_cost = To_cost_con = hilbcd2 = hilbcd = slope1 = nos1 = intervl2 = None
    if 'highest_elevation1' in request.form and  request.form['highest_elevation1'].strip():
        highest_elevation1 = float(request.form['highest_elevation1'])
    else:
            highest_elevation1 = 0
   
    if 'lowest_elevation1' in request.form and  request.form['lowest_elevation1'].strip():
         lowest_elevation1 = float(request.form['lowest_elevation1'])
      
    else:
            lowest_elevation1 = 0
    lbcdlength = float(request.form.get('lbcdlength', 0))
    wos_input = request.form.get('wos',0)
    wos = float(wos_input) if wos_input.strip() else 0
    dos_input = request.form.get('dos',0)
    dos = float(dos_input) if dos_input.strip() else 0

    tw = 0.6
    hos = round((0.66 * dos), 2)
    z1 = 1.5
    z2 = 2
    ed = highest_elevation1 - lowest_elevation1
    if lbcdlength:
        hilbcd = round(np.sqrt((lbcdlength * lbcdlength) - (ed * ed)), 2)
        if hilbcd != 0:
            slope = round((ed / hilbcd) * 100, 2)
            lnselbcd = round(((-2.27) + (1.38 * (np.log(slope))) - (0.56 * np.log(dos)) + (0.25 * np.log(wos))), 2)
            selbcd = round(math.exp(lnselbcd), 2)
            nos = ((slope - selbcd) / dos)

    if nos is not None and not math.isnan(nos):
        nos = round(nos)
        if nos == 1:
            intervl = hilbcd
        else:
            intervl = round(hilbcd / (nos - 1))
        bwoss = round(tw + (hos * z1) + (hos * z2), 2)
        usal = 0.45
        dsal = 0.6
        tbw = round((bwoss + usal + dsal), 2)
        dof = 0.3
        vof = round((dof * tbw * wos), 2)
        doc = 0.6
        voc = round((wos * doc * usal) + ((wos + 0.9) * tw * doc) + (wos + 0.9) * doc * dsal, 2)
        voss = round((((tw + bwoss) / 2) * hos) * wos, 2)
        dssl = round(np.sqrt(hos ** 2 + (z2 * hos) ** 2), 2)
        vow = round((dssl * dsal * tw * 2), 2)
        tvots = round((voc + voss + vof + vow), 2)
        sur_and_demar = 345 * 4
        cost_for_dig_found = round(vof * 242.31, 2)
        cost_ston_pack = round(vof * 1934.75, 2)
        cost_for_stp_sup = round(voss * 1532.52, 2)
        sub_to_cost = round(sur_and_demar + cost_for_dig_found + cost_ston_pack + cost_for_stp_sup, 2)
        cntgency_of_st = round(sub_to_cost * 0.01, 2)
        total_cost = round(sub_to_cost + cntgency_of_st, 2)
        To_cost_con = round(total_cost * nos, 2)

    return render_template('DLT_index.html', highest_elevation1=highest_elevation1, lbcdlength=lbcdlength,
                           lowest_elevation1=lowest_elevation1, wos=wos, dos=dos, tw=tw, hos=hos,
                           z1=z1, z2=z2, ed=ed, lnselbcd=lnselbcd, selbcd=selbcd, nos=nos,
                           intervl=intervl, slope=slope, slope1=slope1, hilbcd=hilbcd, bwoss=bwoss,
                           usal=usal, dsal=dsal, tbw=tbw, dof=dof, vof=vof, doc=doc, voc=voc, voss=voss,
                           dssl=dssl, vow=vow, tvots=tvots, sur_and_demar=sur_and_demar,
                           cost_for_dig_found=cost_for_dig_found, cost_ston_pack=cost_ston_pack,
                           cost_for_stp_sup=cost_for_stp_sup, sub_to_cost=sub_to_cost,
                           cntgency_of_st=cntgency_of_st, total_cost=total_cost, To_cost_con=To_cost_con,
                           hilbcd2=hilbcd2, intervl2=intervl2)


@app.route('/gs', methods=['POST'])
def gs():
    higs = slope = lnsegs = segs = nos = intervl = hoss = vor = aow = sur_and_demar = cost_ston_pack = cost_wire_mesh = sub_to_cost = cntgency_of_st = total_cost = To_cost_con = None

    if 'highest_elevation2' in request.form and  request.form['highest_elevation2'].strip():
        highest_elevation2 = float(request.form['highest_elevation2'])
    else:
            highest_elevation2 = 0
   
    if 'lowest_elevation2' in request.form and  request.form['lowest_elevation2'].strip():
         lowest_elevation2 = float(request.form['lowest_elevation2'])
      
    else:
            lowest_elevation2 = 0
            
    bcdlength1 = float(request.form.get('bcdlength1', 0))
    wos = float(request.form['wos'])
    dos = float(request.form['dos'])
    ed = highest_elevation2 - lowest_elevation2
    higs = round(math.sqrt((bcdlength1 * bcdlength1) - (ed * ed)), 2)
    if dos != 0:
        if wos != 0:
            if higs != 0:
                slope = round((ed / higs) * 100, 2)
                lnsegs = round(((-2.27) + (1.38 * (np.log(slope))) - (0.56 * np.log(dos)) + (0.25 * np.log(wos))), 2)
                segs = round(math.exp(lnsegs), 2)
                nos = round((slope - segs) / dos)
    else:
          nos=0  
    if nos == 1:
        intervl = higs
    else:
        intervl = round( higs / (nos - 1))
    hoss = round(0.66 * dos, 2)
    h = round( wos)
    aprn_len = round(2*hoss, 2)
    sup_strucm3 = round((h*1*hoss)*1.2, 2)
    aprnm3 = round(0.3*aprn_len*h, 2)
    vor = round(sup_strucm3+aprnm3, 2)
    sup_struc = round((2*h*hoss)+(2*1*hoss)+(2*h*1), 2)
    aprn = round((2*0.3*h)+(2*0.3*aprn_len)+(2*aprn_len*h), 2)
    aow = round(sup_struc+aprn, 2)
    sur_and_demar = 345 * 4
    cost_ston_pack = round(vor * 1532.52, 2)
    cost_wire_mesh = round(aow * 449.2, 2)
    sub_to_cost = round(sur_and_demar + cost_ston_pack + cost_wire_mesh, 2)
    cntgency_of_st = round(sub_to_cost * 0.01, 2)
    total_cost = round(sub_to_cost + cntgency_of_st, 2)
    To_cost_con = round(total_cost * nos, 2)

    return render_template('DLT_index.html', highest_elevation2=highest_elevation2, lowest_elevation2=lowest_elevation2,
                           bcdlength1=bcdlength1, wos=wos, dos=dos, ed=ed, lnsegs=lnsegs, segs=segs, nos=nos,
                           intervl=intervl, slope=slope, higs=higs, hoss=hoss,h=h,aprn_len=aprn_len, sup_strucm3=sup_strucm3,aprnm3=aprnm3,vor=vor,sup_struc=sup_struc,aprn=aprn, aow=aow,
                           sur_and_demar=sur_and_demar, cost_ston_pack=cost_ston_pack,
                           cost_wire_mesh=cost_wire_mesh, sub_to_cost=sub_to_cost,
                           cntgency_of_st=cntgency_of_st, total_cost=total_cost, To_cost_con=To_cost_con)


@app.route('/contourstone', methods=['GET', 'POST'])
def page():
    s = r = vi = hi = TL = h = h1 = thob = b = Bt = Af = As = vocsb = ewif = Ec = sbc = tec = None
    show_results = False  # Initialize show_results flag to False.

    if request.method == 'POST':
        s = float(request.form['s'])
        if s!= 0:
            if hi!= 0:
                if vi!=0:
                    r = float(request.form['r'])
                    h = float(request.form['h'])
                    h1 = float(request.form['h1'])
                    Bt = float(request.form['Bt'])
                    
                    if r >= 1500:
                        vi = round((s / 10) + 1.5, 2)
                    else:
                        vi = round((s / 10) + 2, 2)
                    hi = round(vi / s * 100, 2)
                    TL = round(100 * s / vi, 2)
                    thob = round(h + h1, 2)
                    b = round(2 * h / 3, 2)
                    if b <= 0.8:
                        b = 0.8
                    Af = round(b * h1, 2) 
                    As = round((Bt + b) / 2 * h, 2)
                    vocsb = round((Af + As) * TL, 2)
                    ewif = round((TL * b) * h, 2)
                    Ec = round((ewif * 250), 2)
                    sbc = round((vocsb * 500), 2)
                    tec = round((Ec + sbc), 2)
        
        show_results = True  # Set the flag to True to indicate that results should be displayed.
    return render_template('csb_index.html', s=s, r=r, vi=vi, hi=hi, TL=TL, h=h, h1=h1, thob=thob, b=b, Bt=Bt, Af=Af, As=As, vocsb=vocsb, ewif=ewif, Ec=Ec, sbc=sbc, tec=tec, show_results=show_results)



@app.route('/contourbund', methods=['GET', 'POST'])
def page1():
    s = vi = hi = r = z = d = w = fb = zs = B = T = a = lbh = vew = add20 = cost = cbph = soil_dict = soil_dict1 = soil_dict2 = None
    selected = ""
    selected_soil = ""
    show_results = False
    Default_value1 = 1
    Default_value2 = 1.5
    Default_value3 = 2
    Default_value4 = 3
    Default_value5 = 5
    Default_value6 = 6
    h = 0  # Initialize 'h' with a default value

    if soil_dict1 is None:
        soil_dict2 = {
            "selected_option1": "CLAY",
            "selected_option2": "LOAMY",
            "selected_option3": "SANDY",
        }
        soil_dict1 = {
            "selected_option1": Default_value1,
            "selected_option2": Default_value2,
            "selected_option3": Default_value3,
            "selected_option4": Default_value4,
            "selected_option5": Default_value5,
            "selected_option6": Default_value6,
        }
        

    # Get the user-entered soil slope values
    selected_soil_slope1 = float(request.form.get('selected_soil_slope1', soil_dict1['selected_option1']))
    selected_soil_slope2 = float(request.form.get('selected_soil_slope2', soil_dict1['selected_option2']))
    selected_soil_slope3 = float(request.form.get('selected_soil_slope3', soil_dict1['selected_option3']))
    selected_soil_slope4 = float(request.form.get('selected_soil_slope4', soil_dict1['selected_option4']))
    selected_soil_slope5 = float(request.form.get('selected_soil_slope5', soil_dict1['selected_option5']))
    selected_soil_slope6 = float(request.form.get('selected_soil_slope6', soil_dict1['selected_option6']))
    soil_dict1 = {
        "selected_option1": selected_soil_slope1,
        "selected_option2": selected_soil_slope2,
        "selected_option3": selected_soil_slope3,
        "selected_option4": selected_soil_slope4,
        "selected_option5": selected_soil_slope5,
        "selected_option6": selected_soil_slope6,
    }

    if request.method == 'POST':
        s = float(request.form['s'])
        if s!= 0:
            if hi!= 0:
                if vi!=0:
                    vi = round((10 * s + 60) / 100, 2)
                    hi = round(vi / s * 100, 2)
                    r = float(request.form['r'])

                    selected_soil = request.form.get('selected_soil', "")

                    fb = float(request.form['fb'])

                    if selected_soil in ["CLAY", "LOAMY", "SANDY"]:
                        if selected_soil == "CLAY":
                            d = round(math.sqrt((2 * (r * hi * vi) / (hi + (soil_dict1['selected_option1'] * vi)))), 2)
                            w = round(((hi * d) / vi) + soil_dict1['selected_option1'] * d, 2)
                            B = round((soil_dict1['selected_option1'] * d) + (soil_dict1['selected_option4'] * d), 2)
                            h = round((1 + fb / 100) * d, 2)
                            T = round((B - (2 * soil_dict1['selected_option1'] * h)), 2)
                        
                        
                        elif selected_soil == "LOAMY":
                            d = round(math.sqrt((2 * (r * hi * vi) / (hi + (soil_dict1['selected_option2'] * vi)))), 2)
                            w = round(((hi * d) / vi) + soil_dict1['selected_option2'] * d, 2)
                            B = round((soil_dict1['selected_option2'] * d) + (soil_dict1['selected_option5'] * d), 2)
                            h = round((1 + fb / 100) * d, 2)
                            T = round((B - (2 * soil_dict1['selected_option2'] * h)), 2)
                            
                        elif selected_soil == "SANDY":
                            d = round(math.sqrt((2 * (r * hi * vi) / (hi + (soil_dict1['selected_option3'] * vi)))), 2)
                            w = round(((hi * d) / vi) + soil_dict1['selected_option3'] * d, 2)
                            B = round((soil_dict1['selected_option3'] * d) + (soil_dict1['selected_option6'] * d), 2)
                            h = round((1 + fb / 100) * d, 2)
                            T = round((B - (2 * soil_dict1['selected_option3'] * h)), 2)
                            

                    a = round(((T + B) / 2) * h, 2)
                    lbh = round((10000 / hi), 2)
                    vew = round((lbh * a), 2)
                    add20 = round((1.2 * vew), 2)
                    cost = float(request.form['cost'])
                    cbph = round(cost * add20, 2)

        show_results = True

    return render_template('sc_index.html', s=s, vi=vi, hi=hi, r=r, w=w, z=z, d=d, fb=fb, h=h, zs=zs, B=B, T=T, a=a, lbh=lbh, vew=vew, add20=add20, cost=cost,
                           cbph=cbph, show_results=show_results, Default_value1=Default_value1, Default_value2=Default_value2, Default_value3=Default_value3,
                           Default_value4=Default_value4, Default_value5=Default_value5, Default_value6=Default_value6, soil_dict=soil_dict, soil_dict1=soil_dict1,
                           selected_soil=selected_soil, selected=selected, soil_dict2=soil_dict2)



@app.route('/trenchbund', methods=['GET', 'POST'])
def page2():
    p = v = si = Dsoil = Wplot = Lplot = PP = RR = cn2 = W = D = X = L = cn3 = λ = s = Ia = Q = A = HiCCT = ViCCT = LtotalCCT = NoTCCTha = Vearth = RoEW = CPA = None
    show_results = True

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
        cn3 = round(cn2*math.exp(0.00673*(100-cn2)), 2)
        if cn3!=0:
            λ = 0.3
            s = round(25400/cn3-254, 2) 
            Ia = λ*s
            Q = round(math.pow((p-Ia), 2)/(p-Ia + s), 1)/10
            A = W * D
            HiCCT = round( A/(v*Q), 2)
            ViCCT = round(si * HiCCT/100, 2)
            LtotalCCT = round((v/100)*(Q/100 * math.pow(10,4))/(A * math.pow(10,-4)))
            NoTCCTha = round(LtotalCCT/Lplot, 2)
            Vearth =round((v/100) * Lplot * Wplot * Q/100, 2)
            RoEW = float(request.form['RoEW'])
            CPA = round(Vearth * RoEW, 2)
        
        show_results = True
    return render_template('trench_index.html', p=p, v=v, si=si,Dsoil=Dsoil,Wplot=Wplot,Lplot=Lplot,PP=PP,RR=RR,cn2=cn2,cn3=cn3,λ=λ,s=s,Ia=Ia,Q=Q,W=W,D=D,A=A,X=X,L=L,HiCCT=HiCCT,ViCCT=ViCCT,LtotalCCT=LtotalCCT,NoTCCTha=NoTCCTha,Vearth=Vearth,RoEW=RoEW,CPA=CPA, show_results=show_results)

@app.route('/staggeredtrench', methods=['GET', 'POST'])
def page3():
     
     p = v = si = Dsoil = Wplot = Lplot = PP = RR = cn2 = W = D = X = L = cn3 = λ = s = Ia = Q = A = HiST = ViST = LtotalST = NoTSTha = Vearth = RoEW = CPA = None
     show_results = True
     if request.method == 'POST':
        p = float(request.form['p'])
        v = float(request.form['v'])
        si = float(request.form['si'])
        Dsoil =float(request.form['Dsoil'])
        Wplot = float(request.form['Wplot'])
        Lplot = float(request.form['Lplot'])
        PP = float(request.form['PP'])
        RR = float(request.form['RR'])
        cn2 = float(request.form['cn2'])
        W = float(request.form['W'])
        D = float(request.form['D'])
        X = float(request.form['X'])
        L = float(request.form['L'])

        cn3 = round(cn2*math.exp(0.00673*(100-cn2)), 2)
        if cn3!=0:
            λ = 0.3
            s = round(25400/cn3-254, 2) 
            Ia = round(λ*s)
            Q = round(math.pow((p-Ia), 2)/(p-Ia + s), 1)/10
            A = W * D
            HiST =round(A/(v*Q*(1 + X/L)), 2)
            ViST = round(si * HiST/100, 2)
            LtotalST = round((v/100)*(Q/100 * math.pow(10,4))/(A * math.pow(10,-4)), 2)
            NoTSTha = round( LtotalST/L, 2)
            Vearth = round((v/100) * Lplot * Wplot * Q/100, 2)
            RoEW = float(request.form['RoEW'])
            CPA = round( Vearth * RoEW, 2)

        show_results = True
     return render_template('staggered_index.html', p=p, v=v, si=si,Dsoil=Dsoil,Wplot=Wplot,Lplot=Lplot,PP=PP,RR=RR,cn2=cn2,cn3=cn3,λ=λ,s=s,Ia=Ia,Q=Q,W=W,D=D,A=A,X=X,L=L,HiST=HiST,ViST=ViST,LtotalST=LtotalST,NoTSTha=NoTSTha,Vearth=Vearth,RoEW=RoEW,CPA=CPA,show_results=show_results)

@app.route('/benchterrace', methods=['GET', 'POST'])
def page4():


    rainfall = Slope = Sr = vi = terrace = hi = bench = Hectare = Cost = None
    show_results = True
    if request.method == 'POST':
        rainfall = float(request.form['rainfall'])
        Slope = float(request.form['Slope'])
        if Slope!=0:
            Sr = float(request.form['Sr'])
            vi = 0.3*(Slope/3+2)
            terrace = round((vi*(100-Slope*Sr)/Slope), 2)
            hi = vi+terrace
            bench = round(10000/hi, 2)
            Hectare = round(1250*vi, 2)
            Cost = Hectare*157.31

        show_results = True
    return render_template('Bench_Terrace_index.html',rainfall=rainfall, Slope=Slope, Sr=Sr, vi=vi, terrace=terrace, hi=hi, bench=bench, Hectare=Hectare, Cost=Cost,show_results=show_results)

@app.route('/fieldbund', methods=['GET', 'POST'])
def page5():
    op_set_hi = 0; bh = 0; selected_option = ""
    selected=""; x = 0; hob = 0; tw = 0
    bw=0; cross_area=0; op_set_hi1=0
    entered_value = 1  # Default value
    entered_value2 = 1.5  # Default value
    entered_value3 = 2  # Default value
    entered_value4 = 0
    entered_value5 = 0
    entered_value6 = 0

    thisdict = {
        "selected_option": "CLAY",
        "selected_option2": "LOAMY",
        "selected_option3": "SANDY"
    }

    thisdict2 = {
        "selected1": "By Field Dimension",
        "selected2": "User Defined Length",
    }

    if request.method == 'POST':
        hob = float(request.form.get('hob', 0))
        tw = float(request.form.get('tw', 0))
        op_set_hi = float(request.form.get('op_set_hi', 0))

        selected_option = request.form.get('select-option', "")
        entered_value = float(request.form.get('entered_value', 1))
        entered_value2 = float(request.form.get('entered_value2', 1.5))
        entered_value3 = float(request.form.get('entered_value3', 2))

        selected = request.form.get('select-option1', "")
        if 'entered_value4' in request.form and request.form['entered_value4'].strip():
            entered_value4 = float(request.form['entered_value4'])
        else:
            entered_value4 = 0

        if 'entered_value5' in request.form and request.form['entered_value5'].strip():
            entered_value5 = float(request.form['entered_value5'])
        else:
            entered_value5 = 0

        if 'entered_value6' in request.form and request.form['entered_value6'].strip():
            entered_value6 = float(request.form['entered_value6'])
        else:
            entered_value6 = 0



        
        op_set_hi1 = op_set_hi / 100
        bh = round((op_set_hi1 * hob) + hob, 2)

        if selected_option in ["CLAY", "LOAMY", "SANDY"]:
                if selected_option == "CLAY":
                    bw = round(tw + (2 * entered_value * bh), 2)
                elif selected_option == "LOAMY":
                    bw = round(tw + (2 * entered_value2 * bh), 2)
                elif selected_option == "SANDY":
                    bw = round(tw + (2 * entered_value3 * bh), 2)


        cross_area = round(0.5 * (tw + bw) * bh, 2)

        if selected == "By Field Dimension":
            x = round((cross_area * (entered_value4 + entered_value5) * 2), 2)
        elif selected == "User Defined Length":
            x = round(entered_value6 * cross_area, 2)

    return render_template('FieldBund_index.html', thisdict2=thisdict2, my_dict=thisdict, selected_option=selected_option,
                           selected=selected, x=x, hob=hob, tw=tw, op_set_hi=op_set_hi,
                           bh=bh, bw=bw, cross_area=cross_area, op_set_hi1=op_set_hi1,
                           entered_value4=entered_value4, entered_value5=entered_value5,
                           entered_value6=entered_value6, entered_value=entered_value,
                           entered_value2=entered_value2, entered_value3=entered_value3)

      
     
if __name__ == '__main__':
    app.run(debug=True)


