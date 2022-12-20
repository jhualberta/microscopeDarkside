dirInput = getDirectory("~/MyGithub/microscopeDarkside/pic/");
dirOutput = getDirectory("~/MyGithub/microscopeDarkside/resultsImageJ/");
list = getFileList(dirInput);
list = Array.sort(list);
setBatchMode(true);
suffix = ".png"
for (i=0; i<list.length; i++) {
	showProgress(i+1, list.length);
    	open(dirInput+list[i]);
        // print(list[i]);
    	run("8-bit");
        run("Gaussian Blur...", "sigma=1");
        run("Subtract Background...","rolling=50.0 light background");
	run("Set Measurements...", "area mean standard min centroid perimeter fit feret's");
    	setAutoThreshold("Default");
        // run("Analyze Particles...", "  show=Overlay clear");
    	//run("Threshold...");
    	getThreshold(lower, upper);
    	if (upper>90) 
        {
           setThreshold(50, 245);
           //run("Convert to Mask");
           //run("Close");
           run("Analyze Particles...", "size=0-Infinity circularity=0.00-1.00");// show=Nothing display clear summarize");
           saveAs("Results", dirOutput+File.nameWithoutExtension+"_Results.csv");
           //saveAs("Results", dirOutput+String.pad(list[i],4)+"_Results.csv");
           saveAs("TIFF", dirOutput+list[i]);
    	}
    	else {
    		setAutoThreshold("Default");
    		run("Convert to Mask");
    		run("Close");
    		run("Analyze Particles...", "size=0-Infinity circularity=0.00-1.00");// show=Nothing display clear summarize");
   
    	}
    close();
}




