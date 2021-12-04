/**
 * @author Ashish Singh
 * LoanCalculator.java
 * Created on Apr 24, 2020
 */

/*
 * --module-path "/Users/ashishsingh/Documents/Documents - Ashish’s MacBook Pro/Git Hub/MiniProjects/Desktop App/javafx-sdk-15.0.1/lib" --add-modules javafx.controls,javafx.fxml
 */
import javafx.application.*;
import javafx.stage.*;
import javafx.scene.*;
import javafx.scene.layout.*;
import javafx.scene.control.*;
import javafx.geometry.*;
import javafx.event.*;
import javafx.util.converter.DoubleStringConverter;


public class LoanCalculator extends Application
{

    public static void main(String[] args)
    {
        // Start the JavaFX application by calling launch().
        launch(args);
    }
    
    /**
     * @param loanCalcStage
     * Provides the overridden start method with a stage class.
     * The loanCalcStage will be used to set title to the stage,
     * create a loan calculator module, and once the application is
     * run, show the module to the user.
     */
    public void start(Stage loanCalcStage)
    {
        // Gives the application stage a title.
        loanCalcStage.setTitle("Loan Calculator");
        
        // Creates the loan calculator module with the necessary
        // scene and nodes.
        createLoanCalcModule(loanCalcStage);
        
        // Show the stage and its scene.
        loanCalcStage.show();   
    }
    
    /**
     * @param loanCalc
     * loanCalc will be used to set the scene on the stage.
     */
    public void createLoanCalcModule(Stage loanCalc)
    {        
        /*
         * Create a label for Annual Interest Rate
         * Create a text field to capture user's input Annual Interest Rate
         * Forces the data entered in the airtText field to be a numeric value.
         * If alphabetic values are entered, it will be cleared and set to empty.
         */
        Label airLabel = new Label("Annual Interest Rate: ");
        TextField airText = new TextField();
        airText.setTextFormatter(new TextFormatter<>(new DoubleStringConverter()));
        
        /*
         * Create a label for Number of Years.
         * Create a text field to capture user's input for Number of Years.
         * Forces the data entered in the numYearsText field to be a numeric value.
         * If alphabetic values are entered, it will be cleared and set to empty.
         */
        Label numYearsLabel = new Label("Number of Years: ");
        TextField numYearsText = new TextField();
        numYearsText.setTextFormatter(new TextFormatter<>(new DoubleStringConverter()));
        
        /*
         * Create a label for Loan Amount.
         * Create a text field to capture user's input for Loan Amount.
         * Forces the data entered in the loanAmtText field to be a numeric value.
         * If alphabetic values are entered, it will be cleared and set to empty.
         */
        Label loanAmtLabel = new Label("Loan Amount: ");
        TextField loanAmtText = new TextField();
        loanAmtText.setTextFormatter(new TextFormatter<>(new DoubleStringConverter()));
        
        /*
         * Create a label for Monthly Payment.
         * Create a text field for the Monthly Payment to be calculated.
         * The Monthly Payment text field will be "read-only".
         */
        Label monthlyPmtLabel = new Label("Monthly Payment: ");
        TextField monthlyPmtText = new TextField();
        monthlyPmtText.setEditable(false);    
        
        /*
         * Create a label for Total Payment.
         * Create a text field for the Total Payment to be calculated.
         * The Total Payment text field will be "read-only".
         */
        Label totalPmtLabel = new Label("Total Payment: ");
        TextField totalPmtText = new TextField();
        totalPmtText.setEditable(false);  
        
        // Create a button to calculate the monthly and total payment.
        Button calcButton = new Button("Calculate");
        
        // This inner class sets the event handler and the actions to be performed
        // once the calculate button is hit.
        class LoanButtonEvent implements EventHandler<ActionEvent> 
        {
            public void handle(ActionEvent ae)
            {
                double monthlyPmt;    // Variable to store the monthly payment of type double.
                String monthlyPmtStr;    // Variable to store the monthly payment of type string.
                double totalPmt;    // Variable to store the total payment of type double.
                double periods = 12.0;    // Variable for periods initialized for twelve months in a year.
                
                // Stores the calculated monthly payment in type string.
                monthlyPmtStr = monthlyPmtCalc(airText, loanAmtText, numYearsText);
                
                // Sets the monthly payment string in the monthly payment text field.
                monthlyPmtText.setText(monthlyPmtStr);
                
                // Converts the monthly payment of type String to type Double and stores it in the variable.
                monthlyPmt = Double.parseDouble(monthlyPmtStr);
                
                // Calculates the total payment of loan by converting the number of years from type String to type Double.
                totalPmt = Math.round(Double.parseDouble(numYearsText.getText()) * periods * monthlyPmt * 100) / 100.00;
                
                // Sets the total payment string in the total payment text field.
                totalPmtText.setText(String.valueOf(totalPmt));
            }
        }
        
        // Creates a new calcLoan object of the LoanButtonEvent type.
        LoanButtonEvent calcLoan = new LoanButtonEvent();
        
        // Handle action events for the calculate button.
        calcButton.setOnAction(calcLoan);
        
        // Create a scene with specified width and height.
        Scene calcScene = new Scene(gridLayout( airLabel, 
                                                airText, 
                                                numYearsLabel, 
                                                numYearsText,
                                                loanAmtLabel,
                                                loanAmtText,
                                                monthlyPmtLabel,
                                                monthlyPmtText,
                                                totalPmtLabel,
                                                totalPmtText,
                                                calcButton ), 318, 220);
        
        // Set the scene on the stage.
        loanCalc.setScene(calcScene);
    }
    
    /**
     * @param airLabel
     * Label for the annual interest rate.
     * 
     * @param airText
     * Text field to capture the user entered annual interest rate.
     * 
     * @param numYearsLabel
     * Label for the number of years
     * 
     * @param numYearsText
     * Text field to capture the user entered number of years for payment calculation.
     * 
     * @param loanAmtLabel
     * Label for loan amount.
     * 
     * @param loanAmtText
     * Text field to capture the user entered loan amount.
     * 
     * @param monthlyPmtLabel
     * Label for monthly payment.
     * 
     * @param monthlyPmtText
     * Text field to show the calculated monthly payment of the loan.
     * 
     * @param totalPmtLabel
     * Label for total payment.
     * 
     * @param totalPmtText
     * Text field to show the calculated total payment of the loan.
     * 
     * @param calcButton
     * Button to execute the monthly and total loan payment.
     * 
     * @return gridPane
     * Returns the grid pane with alignment, padding, gaps, and nodes with its specified positions.
     */
    public GridPane gridLayout( Label airLabel, 
                                TextField airText,
                                Label numYearsLabel,
                                TextField numYearsText,
                                Label loanAmtLabel,
                                TextField loanAmtText,
                                Label monthlyPmtLabel,
                                TextField monthlyPmtText,
                                Label totalPmtLabel,
                                TextField totalPmtText,
                                Button calcButton )
    {
        // Use a grid pane for the loan calculator stage.
        GridPane gridPane = new GridPane();
        
        /*
         * Setting the padding
         * First is for top of the box
         * Second for right of the box
         * third is for bottom of the box
         * and forth is for left of the box
         */
        gridPane.setPadding(new Insets(10, 10, 5, 20));
        
        // Setting the vertical and horizontal gaps between the columns and rows.
        gridPane.setVgap(5);
        gridPane.setHgap(5);
        
        // Sets the grid alignment        
        gridPane.setAlignment(Pos.TOP_LEFT);
        
        // Adds the label and text fields to the grid pane.
        gridPane.add(airLabel, 0, 0);
        gridPane.add(airText, 1, 0);
        gridPane.add(numYearsLabel, 0, 1);
        gridPane.add(numYearsText, 1, 1);
        gridPane.add(loanAmtLabel, 0, 2);
        gridPane.add(loanAmtText, 1, 2);
        gridPane.add(monthlyPmtLabel, 0, 3);
        gridPane.add(monthlyPmtText, 1, 3);
        gridPane.add(totalPmtLabel, 0, 4);
        gridPane.add(totalPmtText, 1, 4);
        gridPane.add(calcButton, 1, 5);
        
        return gridPane;
    }
    
    /**
     * @param airText
     * Text field to capture the user entered annual interest rate.
     * 
     * @param loanAmtText
     * Text field to capture the user entered loan amount.
     * 
     * @param numYearsText
     * Text field to capture the user entered number of years for payment calculation.
     * 
     * @return monthlyPmt
     * Calculated monthly payment amount of the loan of type string.
     */
    public String monthlyPmtCalc( TextField airText, 
                                  TextField loanAmtText,
                                  TextField numYearsText )
    {
        double rate, i, A, n;    // Variables to store the interest rate, loan amount and the number of years.
        double periods = 12.0;   // Variable to store the 12 months in a year.
        String monthlyPmt;    // Variable to store the monthly payment.
        
        // Stores the user entered value for annual interest rate and converts it to a type Double.
        rate = Double.parseDouble(airText.getText());    
        
        // Stores the user entered value for loan and converts it to a type Double.
        A = Double.parseDouble(loanAmtText.getText());
        
        // Stores the user entered value for number of years, converts it to a type Double, and 
        // converts it to number of months in a year provided by the user.
        n = Double.parseDouble(numYearsText.getText()) * periods;
        
        // Stores the interest rate in a month.
        i = (rate / 100.00) / periods;
        
        // Stores the monthly payment and rounds it to two decimal places.
        monthlyPmt = String.valueOf( Math.round((i * A) / (1 - (Math.pow(1 + i, -n))) * 100) / 100.00 );
        
        // Returns the monthly payment value.
        return monthlyPmt;
    }
}




