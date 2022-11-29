{

   TString dir = gSystem->UnixPathName(gInterpreter->GetCurrentMacroName());
   dir.ReplaceAll("plotDustHist.C","");
   dir.ReplaceAll("/./","/");
   ifstream in;
   in.open("Sample4_center1.dat");//Results_sample4_8Nov_center_10times_Retuned_mmUnits.csv");

   double pyData[] = {1070.2692, 402.688, 166.0604, 96.8,73.4712, 42.108, 33.88,31.5084, 27.6848, 23.3772, 22.6512, 21.6832, 21.296, 20.328, 18.1016, 17.424, 16.456, 16.456, 15.6816, 14.8104, 12.1968, 11.0352, 10.6964, 10.164, 9.4864, 9.4864, 8.8088, 8.8088, 8.8088, 8.1796, 8.1312, 7.5504, 6.9696, 6.9212, 6.3888, 6.3888, 5.8564, 5.8564};

   TH1F *hradius = new TH1F("hradius","",100,0,50);

   TH1F *hradius1 = new TH1F("hradius1","",100,0,50);

   TH1F *hmass = new TH1F("hmass","",100,0,50);

   double totalArea = 0.8*1.2;
   // 2720 x 1824 pixels
   // 0.22 um/px

   double num, area, thresh1, thresh2, thresh3;
   int counts = 0;
   while (1) {
      in >> num >> area>> thresh1>> thresh2>>thresh3;
      if (!in.good()){
	      cout<<"end of the file"<<endl;
	      break;
      }
      // if (nlines < 5) printf("x=%8f, y=%8f, z=%8f\n",x,y,z);
      //
      // area = area*(1000*1000); // mm^2 to um^2
      area = area*0.22*0.22;// px^2 to um^2
      double radius = sqrt(area/TMath::Pi());
      // cout<<radius<<endl;
      hradius->Fill(radius);
      double volume = 4./3*TMath::Pi()*pow(radius,3);
      double mass = volume*0.001;
      hmass->Fill(radius,mass);
      counts++;
   }

   for(int i = 0; i<sizeof(pyData)/sizeof(double); i++)
   {
     double xx = sqrt(pyData[i]/TMath::Pi());
     hradius1->Fill(xx);
   } 

   hradius1->SetLineColor(kRed);

   printf(" found %d dusts\n",counts);
   cout<<"Counts "<<hradius->Integral()<<endl;
   cout<<"Density "<<hmass->Integral()/totalArea/100<<" ng/cm^2"<<endl;

   hradius->SetTitle("For area = 1.2 mm x 0.8 mm");
   hradius->GetYaxis()->SetTitle("Number of particles (/0.5 #mum)");
   hradius->GetXaxis()->SetTitle("Radius of dust particles [#mum]");

   hmass->GetYaxis()->SetTitle("Total mass contribution (ng/0.5 #mum)");
   hmass->GetXaxis()->SetTitle("Radius of dust particles [#mum]");

   TCanvas *c1 = new TCanvas("c1","",1000,600);
   c1->Divide(2,1);
   c1->cd(1);
   hradius->Draw();
   hradius1->Draw("same");

   c1->cd(2);
   hmass->Draw();
  

   in.close();

}
