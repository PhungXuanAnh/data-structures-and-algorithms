import React, { useState, useEffect, useRef } from 'react';
import { Play, Pause, RotateCcw, Plus, Minus, SkipForward } from 'lucide-react';

export default function QuickSortVisualization() {
  const [array, setArray] = useState([]);
  const [sorting, setSorting] = useState(false);
  const [speed, setSpeed] = useState(50);
  const [arraySize, setArraySize] = useState(30);
  const [activeIndices, setActiveIndices] = useState([]);
  const [pivot, setPivot] = useState(null);
  const [partitionRange, setPartitionRange] = useState(null);
  const [sorted, setSorted] = useState([]);
  const [stats, setStats] = useState({ comparisons: 0, swaps: 0 });
  const [currentStep, setCurrentStep] = useState({ action: '', details: '' });
  const [sortStack, setSortStack] = useState([]);
  const [partitionState, setPartitionState] = useState(null);
  const speedRef = useRef(speed);

  useEffect(() => {
    speedRef.current = speed;
  }, [speed]);

  useEffect(() => {
    generateArray();
  }, [arraySize]);

  const generateArray = () => {
    const newArray = Array.from({ length: arraySize }, () => 
      Math.floor(Math.random() * 90) + 10
    );
    setArray(newArray);
    setActiveIndices([]);
    setPivot(null);
    setPartitionRange(null);
    setSorted([]);
    setSortStack([]);
    setPartitionState(null);
    setStats({ comparisons: 0, swaps: 0 });
    setCurrentStep({ action: 'Ready to sort', details: 'Click "Next Step" or "Auto Sort" to begin' });
    setSorting(false);
  };

  const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));

  const partition = async (arr, low, high, isAuto) => {
    const pivotValue = arr[high];
    setPivot(high);
    setPartitionRange([low, high]);
    setCurrentStep({ 
      action: 'Pivot selected', 
      details: `Chose ${pivotValue} at index ${high} as pivot` 
    });
    if (isAuto) await sleep(speedRef.current * 2);

    let i = low - 1;

    for (let j = low; j < high; j++) {
      setActiveIndices([j]);
      setStats(prev => ({ ...prev, comparisons: prev.comparisons + 1 }));
      setCurrentStep({ 
        action: 'Comparing', 
        details: `Is ${arr[j]} ≤ ${pivotValue}? ${arr[j] <= pivotValue ? 'Yes - move to left side' : 'No - stays right'}` 
      });
      if (isAuto) await sleep(speedRef.current);

      if (arr[j] <= pivotValue) {
        i++;
        if (i !== j) {
          const temp1 = arr[i];
          const temp2 = arr[j];
          [arr[i], arr[j]] = [arr[j], arr[i]];
          setArray([...arr]);
          setStats(prev => ({ ...prev, swaps: prev.swaps + 1 }));
          setCurrentStep({ 
            action: 'Swapping', 
            details: `Swapped ${temp2} with ${temp1} - moving smaller element left` 
          });
          if (isAuto) await sleep(speedRef.current);
        }
      }
    }

    [arr[i + 1], arr[high]] = [arr[high], arr[i + 1]];
    setArray([...arr]);
    setStats(prev => ({ ...prev, swaps: prev.swaps + 1 }));
    setCurrentStep({ 
      action: 'Pivot placed', 
      details: `Pivot ${pivotValue} is now at index ${i + 1} in its final position` 
    });
    if (isAuto) await sleep(speedRef.current * 2);

    setSorted(prev => [...prev, i + 1]);
    setPivot(null);
    setActiveIndices([]);
    setPartitionRange(null);

    return i + 1;
  };

  const quickSortIterative = async (arr, isAuto) => {
    const stack = [[0, arr.length - 1]];

    while (stack.length > 0) {
      const [low, high] = stack.pop();

      if (low < high) {
        setPartitionRange([low, high]);
        setCurrentStep({ 
          action: 'Partitioning range', 
          details: `Working on subarray from index ${low} to ${high}` 
        });
        if (isAuto) await sleep(speedRef.current);

        const pi = await partition(arr, low, high, isAuto);

        stack.push([pi + 1, high]);
        stack.push([low, pi - 1]);
      } else if (low === high && low >= 0 && !sorted.includes(low)) {
        setSorted(prev => [...prev, low]);
        setCurrentStep({ 
          action: 'Single element', 
          details: `Element ${arr[low]} at index ${low} is already sorted` 
        });
        if (isAuto) await sleep(speedRef.current);
      }
    }
  };

  const autoSort = async () => {
    setSorting(true);
    const arr = [...array];
    
    if (sortStack.length === 0) {
      setStats({ comparisons: 0, swaps: 0 });
      setSorted([]);
      setCurrentStep({ action: 'Starting', details: 'Beginning Quick Sort algorithm...' });
    }
    
    await quickSortIterative(arr, true);
    
    setSorting(false);
    setActiveIndices([]);
    setPivot(null);
    setPartitionRange(null);
    setSortStack([]);
    setCurrentStep({ action: 'Complete!', details: 'Array is now fully sorted in ascending order.' });
  };

  const nextStep = async () => {
    if (sorting) return;
    
    setSorting(true);
    let arr = [...array];
    let stack = [...sortStack];
    let pState = partitionState;
    
    // Initialize sorting
    if (stack.length === 0 && !pState) {
      setStats({ comparisons: 0, swaps: 0 });
      setSorted([]);
      stack = [[0, arr.length - 1]];
      setSortStack(stack);
      setCurrentStep({ action: 'Starting', details: 'Beginning Quick Sort - click Next Step to continue' });
      setSorting(false);
      return;
    }
    
    // Continue partitioning if in progress
    if (pState) {
      const { low, high, pivotValue, i, j } = pState;
      
      // Show comparison
      if (j < high) {
        setActiveIndices([j]);
        setPivot(high);
        setPartitionRange([low, high]);
        setStats(prev => ({ ...prev, comparisons: prev.comparisons + 1 }));
        setCurrentStep({ 
          action: 'Comparing', 
          details: `Is ${arr[j]} ≤ ${pivotValue}? ${arr[j] <= pivotValue ? 'Yes - move to left side' : 'No - stays right'}` 
        });
        
        let newI = i;
        if (arr[j] <= pivotValue) {
          newI = i + 1;
          if (newI !== j) {
            const temp1 = arr[newI];
            const temp2 = arr[j];
            [arr[newI], arr[j]] = [arr[j], arr[newI]];
            setArray([...arr]);
            setStats(prev => ({ ...prev, swaps: prev.swaps + 1 }));
            setCurrentStep({ 
              action: 'Swapping', 
              details: `Swapped ${temp2} with ${temp1} - moving smaller element left` 
            });
          }
        }
        
        setPartitionState({ low, high, pivotValue, i: newI, j: j + 1 });
        setSorting(false);
        return;
      }
      
      // Finish partition - place pivot
      [arr[i + 1], arr[high]] = [arr[high], arr[i + 1]];
      setArray([...arr]);
      setStats(prev => ({ ...prev, swaps: prev.swaps + 1 }));
      
      const pi = i + 1;
      setSorted(prev => [...prev, pi]);
      setPivot(null);
      setActiveIndices([]);
      setPartitionRange(null);
      
      setCurrentStep({ 
        action: 'Pivot placed', 
        details: `Pivot ${pivotValue} is now at index ${pi} in its final position` 
      });
      
      stack.push([pi + 1, high]);
      stack.push([low, pi - 1]);
      setSortStack(stack);
      setPartitionState(null);
      setSorting(false);
      return;
    }
    
    // Start new partition
    const [low, high] = stack.pop();
    
    if (low < high) {
      const pivotValue = arr[high];
      setPivot(high);
      setPartitionRange([low, high]);
      setCurrentStep({ 
        action: 'Pivot selected', 
        details: `Chose ${pivotValue} at index ${high} as pivot for range [${low}, ${high}]` 
      });
      
      setPartitionState({ low, high, pivotValue, i: low - 1, j: low });
      setSortStack(stack);
      setSorting(false);
      return;
    } else if (low === high && low >= 0 && !sorted.includes(low)) {
      setSorted(prev => [...prev, low]);
      setCurrentStep({ 
        action: 'Single element', 
        details: `Element ${arr[low]} at index ${low} is already sorted` 
      });
      setSortStack(stack);
      setSorting(false);
      return;
    } else {
      setSortStack(stack);
      if (stack.length === 0 && !partitionState) {
        setCurrentStep({ action: 'Complete!', details: 'Array is now fully sorted in ascending order.' });
        setPivot(null);
        setActiveIndices([]);
        setPartitionRange(null);
      }
      setSorting(false);
      return;
    }
  };

  const getBarColor = (index) => {
    if (sorted.includes(index)) return 'bg-green-500';
    if (pivot === index) return 'bg-red-500';
    if (activeIndices.includes(index)) return 'bg-yellow-500';
    if (partitionRange && index >= partitionRange[0] && index <= partitionRange[1]) return 'bg-blue-400';
    return 'bg-gray-400';
  };

  const maxValue = Math.max(...array, 1);

  return (
    <div className="w-full min-h-screen bg-gradient-to-br from-slate-900 to-slate-800 p-8">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-6">
          <h1 className="text-4xl font-bold text-white mb-2">Quick Sort Visualization</h1>
          <p className="text-slate-300">Watch the divide-and-conquer algorithm partition the array</p>
        </div>

        <div className="bg-slate-700/50 rounded-lg p-4 border border-slate-600 mb-6">
          <h3 className="text-lg font-semibold text-white mb-2">Current Step</h3>
          <div className="space-y-2">
            <div>
              <span className="text-blue-400 font-semibold">Action: </span>
              <span className="text-white">{currentStep.action}</span>
            </div>
            <div>
              <span className="text-blue-400 font-semibold">Details: </span>
              <span className="text-slate-300">{currentStep.details}</span>
            </div>
          </div>
        </div>

        <div className="bg-slate-800/50 rounded-xl p-6 backdrop-blur-sm border border-slate-700 mb-6" style={{ minHeight: '400px' }}>
          <div className="h-full flex items-end justify-center gap-0.5 pb-8">
            {array.map((value, index) => (
              <div key={index} className="flex flex-col items-center justify-end flex-1 min-w-0">
                <div
                  className={`w-full ${getBarColor(index)} transition-all duration-300 rounded-t flex items-start justify-center pt-1`}
                  style={{ height: `${value * 3}px` }}
                >
                  <span className="text-xs font-semibold text-white">{value}</span>
                </div>
                <span className="text-xs text-slate-500 mt-1 truncate w-full text-center">{index}</span>
              </div>
            ))}
          </div>
        </div>

        <div className="grid grid-cols-2 gap-4 mb-6">
          <div className="bg-slate-700/50 rounded-lg p-3 text-center">
            <div className="text-slate-400 text-sm">Comparisons</div>
            <div className="text-white text-xl font-bold">{stats.comparisons}</div>
          </div>
          <div className="bg-slate-700/50 rounded-lg p-3 text-center">
            <div className="text-slate-400 text-sm">Swaps</div>
            <div className="text-white text-xl font-bold">{stats.swaps}</div>
          </div>
        </div>

        <div className="grid grid-cols-3 gap-3 mb-4">
          <button
            onClick={autoSort}
            disabled={sorting}
            className="bg-green-600 hover:bg-green-700 disabled:bg-slate-600 text-white px-6 py-3 rounded-lg font-semibold flex items-center justify-center gap-2 transition-colors"
          >
            {sorting ? <Pause size={20} /> : <Play size={20} />}
            {sorting ? 'Sorting...' : 'Auto Sort'}
          </button>
          <button
            onClick={nextStep}
            disabled={sorting}
            className="bg-purple-600 hover:bg-purple-700 disabled:bg-slate-600 text-white px-6 py-3 rounded-lg font-semibold flex items-center justify-center gap-2 transition-colors"
          >
            <SkipForward size={20} />
            Next Step
          </button>
          <button
            onClick={generateArray}
            disabled={sorting}
            className="bg-blue-600 hover:bg-blue-700 disabled:bg-slate-600 text-white px-6 py-3 rounded-lg font-semibold flex items-center justify-center gap-2 transition-colors"
          >
            <RotateCcw size={20} />
            New Array
          </button>
        </div>

        <div className="grid grid-cols-2 gap-3 mb-4">
          <div className="bg-slate-700/50 rounded-lg p-4">
            <label className="text-slate-300 text-sm mb-2 block">Array Size: {arraySize}</label>
            <div className="flex items-center gap-2">
              <button
                onClick={() => setArraySize(Math.max(10, arraySize - 5))}
                disabled={sorting}
                className="bg-slate-600 hover:bg-slate-500 disabled:bg-slate-700 text-white p-2 rounded transition-colors"
              >
                <Minus size={16} />
              </button>
              <input
                type="range"
                min="10"
                max="50"
                value={arraySize}
                onChange={(e) => setArraySize(Number(e.target.value))}
                disabled={sorting}
                className="flex-1"
              />
              <button
                onClick={() => setArraySize(Math.min(50, arraySize + 5))}
                disabled={sorting}
                className="bg-slate-600 hover:bg-slate-500 disabled:bg-slate-700 text-white p-2 rounded transition-colors"
              >
                <Plus size={16} />
              </button>
            </div>
          </div>

          <div className="bg-slate-700/50 rounded-lg p-4">
            <label className="text-slate-300 text-sm mb-2 block">Speed: {speed}ms</label>
            <div className="flex items-center gap-2">
              <button
                onClick={() => setSpeed(Math.max(10, speed - 20))}
                className="bg-slate-600 hover:bg-slate-500 text-white p-2 rounded transition-colors"
              >
                <Minus size={16} />
              </button>
              <input
                type="range"
                min="10"
                max="300"
                step="10"
                value={speed}
                onChange={(e) => setSpeed(Number(e.target.value))}
                className="flex-1"
              />
              <button
                onClick={() => setSpeed(Math.min(300, speed + 20))}
                className="bg-slate-600 hover:bg-slate-500 text-white p-2 rounded transition-colors"
              >
                <Plus size={16} />
              </button>
            </div>
          </div>
        </div>

        <div className="flex gap-6 justify-center text-sm mb-4 flex-wrap">
          <div className="flex items-center gap-2">
            <div className="w-4 h-4 bg-gray-400 rounded"></div>
            <span className="text-slate-300">Unsorted</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-4 h-4 bg-blue-400 rounded"></div>
            <span className="text-slate-300">Current Partition</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-4 h-4 bg-yellow-500 rounded"></div>
            <span className="text-slate-300">Comparing</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-4 h-4 bg-red-500 rounded"></div>
            <span className="text-slate-300">Pivot</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-4 h-4 bg-green-500 rounded"></div>
            <span className="text-slate-300">Sorted</span>
          </div>
        </div>
      </div>
    </div>
  );
}