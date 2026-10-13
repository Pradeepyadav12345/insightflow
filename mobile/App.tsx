import { StatusBar } from 'expo-status-bar';
import { ScrollView, StyleSheet, Text, View, SafeAreaView } from 'react-native';

const stats = [
  { label: 'Revenue', value: '$125k', delta: '+8.1%' },
  { label: 'Users', value: '24.8k', delta: '+5.4%' },
  { label: 'Insights', value: '89', delta: '+11%' },
];

const segments = [
  { name: 'Enterprise', percent: 82 },
  { name: 'Mid-market', percent: 68 },
  { name: 'SMB', percent: 54 },
];

const reports = [
  { name: 'Q3 Revenue Summary', owner: 'Finance', time: '2h ago' },
  { name: 'Customer Retention', owner: 'Growth', time: '5h ago' },
];

export default function App() {
  return (
    <SafeAreaView style={styles.safeArea}>
      <ScrollView contentContainerStyle={styles.scrollContent}>
        <View style={styles.container}>
          <View style={styles.headerRow}>
            <Text style={styles.badge}>InsightFlow AI</Text>
            <Text style={styles.liveTag}>Live</Text>
          </View>

          <Text style={styles.title}>AI data analyst for your business.</Text>
          <Text style={styles.subtitle}>Ask your data. Get analysis, insights, and reports in one place.</Text>

          <View style={styles.statsGrid}>
            {stats.map((stat) => (
              <View key={stat.label} style={styles.statCard}>
                <Text style={styles.statLabel}>{stat.label}</Text>
                <Text style={styles.statValue}>{stat.value}</Text>
                <Text style={styles.statDelta}>{stat.delta}</Text>
              </View>
            ))}
          </View>

          <View style={styles.panel}>
            <Text style={styles.panelTitle}>Segment health</Text>
            {segments.map((segment) => (
              <View key={segment.name} style={styles.segmentRow}>
                <View style={styles.segmentMeta}>
                  <Text style={styles.segmentName}>{segment.name}</Text>
                  <Text style={styles.segmentPercent}>{segment.percent}%</Text>
                </View>
                <View style={styles.segmentMeter}>
                  <View style={[styles.segmentFill, { width: `${segment.percent}%` }]} />
                </View>
              </View>
            ))}
          </View>

          <View style={styles.panel}>
            <Text style={styles.panelTitle}>Recent reports</Text>
            {reports.map((report) => (
              <View key={report.name} style={styles.reportRow}>
                <View>
                  <Text style={styles.reportName}>{report.name}</Text>
                  <Text style={styles.reportOwner}>{report.owner}</Text>
                </View>
                <Text style={styles.reportTime}>{report.time}</Text>
              </View>
            ))}
          </View>
        </View>
        <StatusBar style="light" />
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: '#07111f',
  },
  scrollContent: {
    paddingVertical: 24,
  },
  container: {
    flex: 1,
    paddingHorizontal: 20,
    paddingBottom: 24,
    backgroundColor: '#07111f',
  },
  headerRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 16,
  },
  badge: {
    backgroundColor: 'rgba(94, 166, 255, 0.12)',
    color: '#7fb4ff',
    borderRadius: 999,
    paddingHorizontal: 12,
    paddingVertical: 8,
    fontSize: 12,
    fontWeight: '700',
    letterSpacing: 1,
    textTransform: 'uppercase',
  },
  liveTag: {
    backgroundColor: 'rgba(56, 200, 142, 0.12)',
    color: '#8af0c2',
    borderRadius: 999,
    paddingHorizontal: 10,
    paddingVertical: 6,
    fontSize: 10,
    fontWeight: '700',
    letterSpacing: 0.8,
    textTransform: 'uppercase',
  },
  title: {
    color: '#f3f7ff',
    fontSize: 30,
    fontWeight: '700',
    marginBottom: 8,
  },
  subtitle: {
    color: '#b9cae3',
    fontSize: 16,
    marginBottom: 20,
  },
  statsGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
    marginBottom: 20,
  },
  statCard: {
    width: '31%',
    minWidth: 110,
    backgroundColor: 'rgba(13, 27, 42, 0.8)',
    borderRadius: 18,
    borderWidth: 1,
    borderColor: 'rgba(163, 186, 255, 0.12)',
    padding: 16,
    marginBottom: 12,
  },
  statLabel: {
    color: '#a7b9d8',
    fontSize: 12,
    textTransform: 'uppercase',
    letterSpacing: 1,
  },
  statValue: {
    color: '#f3f7ff',
    fontSize: 24,
    fontWeight: '700',
    marginTop: 8,
  },
  statDelta: {
    color: '#8af0c2',
    fontSize: 12,
    marginTop: 6,
  },
  panel: {
    backgroundColor: 'rgba(13, 27, 42, 0.8)',
    borderRadius: 18,
    borderWidth: 1,
    borderColor: 'rgba(163, 186, 255, 0.12)',
    padding: 18,
    marginTop: 14,
  },
  panelTitle: {
    color: '#f3f7ff',
    fontSize: 18,
    fontWeight: '700',
    marginBottom: 14,
  },
  segmentRow: {
    marginBottom: 12,
  },
  segmentMeta: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 6,
  },
  segmentName: {
    color: '#dfe9fb',
    fontSize: 14,
  },
  segmentPercent: {
    color: '#8af0c2',
    fontSize: 12,
  },
  segmentMeter: {
    height: 10,
    borderRadius: 999,
    backgroundColor: 'rgba(255,255,255,0.06)',
    overflow: 'hidden',
  },
  segmentFill: {
    height: '100%',
    borderRadius: 999,
    backgroundColor: '#5ea6ff',
  },
  reportRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingVertical: 10,
    borderBottomWidth: 1,
    borderBottomColor: 'rgba(255,255,255,0.05)',
  },
  reportName: {
    color: '#f3f7ff',
    fontSize: 15,
    fontWeight: '600',
  },
  reportOwner: {
    color: '#a7b9d8',
    fontSize: 12,
    marginTop: 2,
  },
  reportTime: {
    color: '#8fb6ff',
    fontSize: 11,
  },
});
