function gera_cor(qtd = 1) {
  var bg_color = [];
  var border_color = [];
  for (let i = 0; i < qtd; i++) {
    let r = Math.random() * 255;
    let g = Math.random() * 255;
    let b = Math.random() * 255;
    bg_color.push(`rgba(${r}, ${g}, ${b}, ${0.2})`);
    border_color.push(`rgba(${r}, ${g}, ${b}, ${1})`);
  }
  return [bg_color, border_color];
}

// Global variable to store the chart type
let selectedGraphType = localStorage.getItem('selectedGraphType') || 'bar'; // Default type

// Chart handler
document.addEventListener("DOMContentLoaded", function () {
  const ctx = document.getElementById("price_chart").getContext("2d");

  function updateChart(type) {
    if (window.myChart) {
      window.myChart.destroy();
    }

    // Django data received from HTML
    const labels = priceData.labels; // Dates
    const data = priceData.data; // Corresponding values (assumed to be in pairs)

    // Concatenate values of reais and centavos
    const totalData = [];

    for (let i = 0; i < data.length; i += 2) {
      const reais = parseFloat(data[i]);
      const centavos = i + 1 < data.length ? parseFloat(data[i + 1]) : 0;

      const total = reais + centavos / 100; // Converts centavos to reais
      totalData.push({ date: labels[i / 2], value: total }); // Adds date and total
    }

    // Sort the data by date (oldest to newest)
    totalData.sort((a, b) => new Date(a.date) - new Date(b.date));

    // Extract the sorted data
    const sortedLabels = totalData.map(item => item.date);
    const sortedValues = totalData.map(item => item.value);

    if (sortedLabels.length === 0 || sortedValues.length === 0) {
      console.error("Labels or data are empty");
      return; // Prevents chart creation if there is no data
    }

    // Generate unique colors for each data point
    const colors = gera_cor(sortedValues.length);

    window.myChart = new Chart(ctx, {
      type: type,
      data: {
        labels: sortedLabels,
        datasets: [
          {
            label: "Maior Valor",
            data: sortedValues,
            backgroundColor: colors[0], // Unique background colors for each bar
            borderColor: colors[1], // Unique border colors for each bar
            borderWidth: 2,
          },
        ],
      },
      options: {
        scales: {
          y: {
            title: {
              display: true,
              text: 'Valor',
            },
          },
          x: {
            title: {
              display: true,
              text: 'Data',
            },
          },
        },
      },
    });
  }

  // Initializes the chart when the page loads.
  updateChart(selectedGraphType);

  // Updates the chart when the selection changes.
  document.getElementById("graphSelect").addEventListener("change", function () {
    selectedGraphType = this.value; // Updates the variable with the selected type.
    localStorage.setItem('selectedGraphType', selectedGraphType); // Stores in localStorage.
    updateChart(selectedGraphType);
  });

  // Logic for the currency form.
  const currencySelect = document.getElementById("currencySelect");

  // Adds an event to automatically submit the form.
  currencySelect.addEventListener("change", function () {
    this.form.submit(); // Submits the form.
  });
});

// Retrieve and set the last selected chart type
document.addEventListener("DOMContentLoaded", function () {
  const graphSelect = document.getElementById("graphSelect");
  const lastSelectedGraph = localStorage.getItem('selectedGraphType');
  
  if (lastSelectedGraph) {
    graphSelect.value = lastSelectedGraph; // Sets the selection in the dropdown.
    updateChart(lastSelectedGraph); // Updates the chart with the last selection.
  }

  // Updates the chart when the selection changes.
  graphSelect.addEventListener("change", function () {
    const selectedGraph = this.value;
    localStorage.setItem('selectedGraphType', selectedGraph); // Stores the new selection.
    updateChart(selectedGraph); // Updates the chart
  });
});
